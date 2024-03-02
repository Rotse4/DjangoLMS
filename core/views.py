from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.serializers import NewsAndSerializer
from .models import NewsAndEvents
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
@api_view(['GET'])
def home_view(request):
    
    items = NewsAndEvents.objects.all().order_by("-updated_date")
    serializer = NewsAndSerializer(items, many= True)
    return Response({"EventsAndNews": serializer.data})


@api_view(["POST"])
def post_add(request):
    title = request.POST.get("title")
    serializer = NewsAndSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response("created successfulyy")
    return Response(serializer.errors)


@api_view(['POST'])
def edit_post(request):
    pass



