from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class PostSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    class Meta:
        model = Post
        fields = ['user', 'id', 'description', 'date_created', 'likes']


class CommentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    class Meta:
        model = Comment
        fields = ['post', 'user', 'id', 'comment', 'date_created', 'likes']
