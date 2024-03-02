from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from course.models import Course
from course.serializers import CourseSerializer


# Create your views here.

@api_view(['GET'])
def get_courses(request):
    courses= Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response({'data': serializer.data})
    