from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ['username', 'email', 'password', 'bio', 'profile_picture']
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    # Use get_user_model().objects.create_user() to create the user
    user = get_user_model().objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password']  # Automatically hashes the password
    )
    
    # Set additional fields
    user.bio = validated_data.get('bio', '')
    user.profile_picture = validated_data.get('profile_picture', None)
    user.save()

    # Create a token for the user
    Token.objects.create(user=user)
    return user

class UserLoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
    user = get_user_model().objects.filter(username=data['username']).first()
    if user and user.check_password(data['password']):
      return user
    raise serializers.ValidationError("Incorrect Credentials")
