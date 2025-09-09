from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

        def create(self, validated_date):
            user = User.objects.create_user(
                username=validated_date['username'],
                email= validated_date['email'],
                password=validated_date['password']

            )
            return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'posts']

    def get_posts(self, obj):
        user_posts = Post.objects.filter(author=obj)
        return [{'id': p.id, 'title': p.title} for p in user_posts]