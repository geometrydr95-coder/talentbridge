from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('talents/', views.talent_list, name='talent_list'),
    path('talents/add/', views.add_talent, name='add_talent'),
    path('talents/<int:pk>/', views.talent_detail, name='talent_detail'),
    path('scholarships/', views.scholarship_list, name='scholarship_list'),
    path('scholarships/<int:pk>/', views.scholarship_detail, name='scholarship_detail'),
]