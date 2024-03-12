from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_courses, name='home_view'),
    path('get_content', views.get_content),
    # path('post/', views.post_add, name='post_add'),
]
