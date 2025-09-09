from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',"is_staff", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_date):
            user = User.objects.create_user(
                username=validated_date['username'],
                email= validated_date['email'],
                password=validated_date['password']

            )
            if validated_data.get("is_staff"):
              user.is_staff = True
            if validated_data.get("is_superuser"):
              user.is_superuser = True
            user.save()
            return user    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()