from django.contrib import admin

from django.utils.html import format_html
from django.utils.text import Truncator
from .models import CourseAllocation, Course,Upload

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('id','title','get_image', 'code', 'credit', 'level', 'summary', 'year', 'semester', 'is_elective',)

    def get_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.picture.url)
    get_image.short_description = 'picture'  

    def short_description(self, obj):
        max_length = 50  # Maximum length of the truncated description
        truncated = Truncator(obj.summary).chars(max_length)
        return truncated 
    

class UploadAdmin(admin.ModelAdmin):
    model = Upload
    list_display = ('title','course', 'get_image','file', 'updated_date', 'upload_time',)

    def get_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.file.url)
    get_image.short_description = 'file'

admin.site.register(Course,CourseAdmin)
admin.site.register(Upload,UploadAdmin)
admin.site.register(CourseAllocation)
# admin.site.register(Semester)

