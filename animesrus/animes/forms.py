from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Anime

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ('anime_name', 'image', 'description', 'language_type', 'on_hulu', 'on_netflix', 'on_crunchyroll', 'on_funamation')