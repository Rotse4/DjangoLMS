from rest_framework import serializers
from .models import Course, Upload

class CourseSerializer(serializers.ModelSerializer):
    # posted_as_display = serializers.CharField(source='get_posted_as_display', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

class UploadSerializer(serializers.ModelSerializer):
    # posted_as_display = serializers.CharField(source='get_posted_as_display', read_only=True)

    class Meta:
        model = Upload
        fields = ['id', 'title', 'file', 'updated_date', 'upload_time']

