from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Quiz, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4  # Number of extra answer fields to display

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'pass_mark')  # Display these fields in the list view
    inlines = [AnswerInline]  # Include answers inline with the quiz in the admin panel

admin.site.register(Quiz, QuizAdmin)