# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Post, Todo, Comment
from .serializers import UserSerializer, PostSerializer, TodoSerializer, CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Artistas
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Albuns
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Músicas
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Músicas
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer