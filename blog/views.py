from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from rest_framework.serializers import Serializer
from rest_framework import generics
from rest_framework.filters import OrderingFilter,SearchFilter
from .serializer import PostListSerializer
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostList(generics.ListAPIView): 
    queryset = Post.objects.all() 
    serializer_class =PostListSerializer
    filter_backends = [SearchFilter,]
    search_fields = ["title"]

class anPost(generics.RetrieveAPIView): 
    queryset = Post.objects.all() 
    serializer_class = PostListSerializer 

class CreatePost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class DelatePost(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer