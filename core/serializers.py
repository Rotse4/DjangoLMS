from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework.serializers import ModelSerializer
from .models import NewsAndEvents

class NewsAndSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAndEvents
        fields = '__all__'

