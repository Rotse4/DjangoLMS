from django.shortcuts import render
from rest_framework.response import Response
from django.contrib import messages
from account.serializers import UserSerializer
from .models import User, Student, Parent
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
# from .serializers import UserRegistrationSerializer


# Create your views here.
def validate_username(request):
    username = request.GET.get("username", None)
    data = {"is_taken": User.objects.filter(username__iexact=username).exists()}
    return Response(data)

@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        messages.success(request,f'Account created successfully')
        Response("Sucessfull")

    else:
        messages.error(request, f"Something went wrong")
        Response("Enter correct details")



@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    