from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Post,Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content',
            'created_at',
            'user'
        ]



class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    comments_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'comments',
            'created_at',
            'comments_count',
            'img'
        ]
    def get_comments_count(self, obj):
        return obj.comments.count()
