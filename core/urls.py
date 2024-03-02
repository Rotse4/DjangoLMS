# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('post/', views.post_add, name='post_add'),
]
