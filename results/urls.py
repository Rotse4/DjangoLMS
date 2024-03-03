# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_answer, name='check-answer'),
    # Other URLs...
    path('questions/', views.get_all_questions, name='get-all-questions'),
]
