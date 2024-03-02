from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    # posted_as_display = serializers.CharField(source='get_posted_as_display', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
