from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the custom user model dynamically
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'password', 'bio', 'profile_picture']
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    # Use create_user to ensure password is hashed
    user = User.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password']  # Password is automatically hashed
    )
    
    # Set additional fields
    user.bio = validated_data.get('bio', '')
    user.profile_picture = validated_data.get('profile_picture', None)
    user.save()
    
    # Create an authentication token for the user
    Token.objects.create(user=user)
    return user

class UserLoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
    user = User.objects.filter(username=data['username']).first()
    if user and user.check_password(data['password']):
      return user
    raise serializers.ValidationError("Incorrect Credentials")
