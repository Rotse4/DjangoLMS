from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from course.models import Course,Upload
from course.serializers import CourseSerializer, UploadSerializer


# Create your views here.

@api_view(['GET'])
def get_courses(request):
    courses= Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response({'data': serializer.data})


@api_view(['Get'])
def get_content(request, pk):
    course=Course.objects.filter(id=pk).first()
    upload=Upload.objects.filter(course=course)

    serializer = UploadSerializer(upload,many=True )
    return Response(serializer.data)
