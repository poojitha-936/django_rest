from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())
    
    class Meta:
        model= Comment
        fields='__all__'


class BlogSerializer(serializers.ModelSerializer):
    blog_title= serializers.CharField(source='blog.title')
    class Meta:
        model= Blog
        fields='__all__'