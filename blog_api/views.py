from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework  import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import filters

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

        return Post.objects.filter(author=user)

class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        print(slug)
        return Post.objects.filter(slug=slug)
    
class PostListDetailFilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class= PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['^slug']   
    
class PostSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']    
    
    
    
    
    
class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryest = Post.objects.all()
    serializer_class = PostSerializer
    
class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class DeletePost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer        