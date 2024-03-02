from django.contrib import admin

from .models import CourseAllocation, Course

# Register your models here.
admin.site.register(CourseAllocation)
admin.site.register(Course)
# admin.site.register(Semester)