from django.contrib import admin

# Register your models here.
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'introduction', 'teacher', 'price')
    search_fields = ('name', 'introduction', 'teacher', 'price')
    list_filter = ('name', 'introduction', 'teacher', 'price')


