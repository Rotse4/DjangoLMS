from rest_framework import serializers
from django.contrib.auth.models import User

# from rest_framework.serializers import ModelSerializer
from .models import User, Student, Parent, DepartmentHead




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentHead
        fields = '__all__'

        
# class RatingSerializer(serializers.Serializer):
#     rating = serializers.IntegerField(min_value=1, max_value=5)


