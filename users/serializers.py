from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'full_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        user = User.objects.create_user(**validated_data)
        user.profile.full_name = full_name
        user.profile.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    role = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'full_name', 'bio', 'image', 'role')
