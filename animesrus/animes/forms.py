from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Anime

class RequestDeleteForm(forms.Form):
    anime_name = forms.CharField(required=True)
    email_address = forms.CharField(required=True)
    reason_for_deletion = forms.CharField(widget=forms.Textarea, required=True)