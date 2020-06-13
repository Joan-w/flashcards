from django import forms
from .models import FlashCard
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
  class Meta:
    model=User
    fields=['username','email', 'password1','password2']

class CommentForm(forms.ModelForm):

    class Meta:
        model = FlashCard
        fields = ('text','title','subject')
        widgets = {
          'text': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }
