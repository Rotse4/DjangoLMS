from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_courses, name='home_view'),
    # path('post/', views.post_add, name='post_add'),
]
