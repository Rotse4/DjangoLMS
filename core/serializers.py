from rest_framework import serializers
from .models import NewsAndEvents

class NewsAndSerializer(serializers.ModelSerializer):
    posted_as_display = serializers.CharField(source='get_posted_as_display', read_only=True)

    class Meta:
        model = NewsAndEvents
        fields = '__all__'
