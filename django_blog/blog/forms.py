from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagField

class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")

class UserProfileForm(forms.ModelForm):
  email = forms.EmailField(required=True)
  class Meta:
    model = User
    fields = ("username", "email")

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ["title", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
      "content": forms.Textarea(
          attrs={"rows": 3, "placeholder": "Add a comment..."}
        ),
    }


class PostForm(forms.ModelForm):
  tags = TagField(required=False)  # This will allow users to add tags

  class Meta:
    model = Post
    fields = ["title", "content", "tags"]
