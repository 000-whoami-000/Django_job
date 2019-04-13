from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# return render(request, 'index.html',{'posts':posts})
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from frontSide.serializers import UserSerializer, GroupSerializer

def index(request):
	posts = Post.objects.all()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


	

