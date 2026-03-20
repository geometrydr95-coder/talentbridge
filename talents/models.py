from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('scout', 'Scout'),
        ('admin', 'Admin'),
        ('organization', 'Scholarship Organization'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    school = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Talent(models.Model):
    CATEGORY_CHOICES = [
        ('sport', 'Sport'),
        ('tech', 'Tech'),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField()
    video = models.FileField(upload_to='videos/', blank=True)
    image = models.ImageField(upload_to='talent_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.student.username}"


class Scholarship(models.Model):
    title = models.CharField(max_length=150)
    organization = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    talent_category = models.CharField(max_length=10, choices=Talent.CATEGORY_CHOICES)
    deadline = models.DateField()
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} -> {self.scholarship.title}"