from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['username', 'email', 'password', 'bio', 'profile_picture']
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = CustomUser(
      email=validated_data['email'],
      username=validated_data['username'],
      bio=validated_data.get('bio', ''),
      profile_picture=validated_data.get('profile_picture', None)
    )
    user.set_password(validated_data['password'])
    user.save()
    Token.objects.create(user=user)
    return user

class UserLoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
    user = CustomUser.objects.filter(username=data['username']).first()
    if user and user.check_password(data['password']):
      return user
    raise serializers.ValidationError("Incorrect Credentials")
