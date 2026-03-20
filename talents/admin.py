from django.contrib import admin
from .models import Profile, Talent, Scholarship, Application

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'school', 'country']

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ['title', 'student', 'category', 'created_at']

@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'talent_category', 'deadline']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['student', 'scholarship', 'status', 'applied_at']