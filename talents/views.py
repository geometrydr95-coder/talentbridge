from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Profile, Talent, Scholarship, Application

def home(request):
    talents = Talent.objects.all().order_by('-created_at')[:6]
    scholarships = Scholarship.objects.all()[:3]
    return render(request, 'talents/home.html', {
        'talents': talents,
        'scholarships': scholarships
    })

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST['role']
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        Profile.objects.create(user=user, role=role)
        messages.success(request, "Account created successfully")
        return redirect('login')
    return render(request, 'talents/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'talents/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'student'}
    )
    talents = Talent.objects.filter(student=request.user)
    context = {
        'profile': profile,
        'talents': talents,
        'talents_count': talents.count(),
        'applications_count': Application.objects.filter(student=request.user).count(),
        'scholarships_count': Scholarship.objects.count()
    }
    return render(request, 'talents/dashboard.html', context)

def talent_list(request):
    talents = Talent.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    category = request.GET.get('category')
    if query:
        talents = talents.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    if category:
        talents = talents.filter(category=category)
    return render(request, 'talents/talent_list.html', {'talents': talents})

def talent_detail(request, pk):
    talent = get_object_or_404(Talent, id=pk)
    return render(request, 'talents/talent_detail.html', {'talent': talent})

@login_required
def add_talent(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        description = request.POST['description']
        image = request.FILES.get('image')
        video = request.FILES.get('video')
        Talent.objects.create(
            student=request.user,
            title=title,
            category=category,
            description=description,
            image=image,
            video=video
        )
        messages.success(request, "Talent added successfully!")
        return redirect('dashboard')
    return render(request, 'talents/add_talent.html')

def scholarship_list(request):
    scholarships = Scholarship.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    category = request.GET.get('category')
    if query:
        scholarships = scholarships.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    if category:
        scholarships = scholarships.filter(talent_category=category)
    return render(request, 'talents/scholarship_list.html', {'scholarships': scholarships})

def scholarship_detail(request, pk):
    scholarship = get_object_or_404(Scholarship, id=pk)
    return render(request, 'talents/scholarship_detail.html', {'scholarship': scholarship})