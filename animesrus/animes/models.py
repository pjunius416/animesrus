from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Anime(models.Model):
    anime_name = models.CharField(max_length=100, blank=False, null=False, default='')
    wiki_url = models.CharField(max_length=100, blank=False, null=False, default='')
    description = models.TextField()
    language_type = models.CharField(max_length=20, blank=False, null=False, default='')
    on_hulu = models.BooleanField(default='')
    on_netflix = models.BooleanField(default='')
    on_crunchyroll = models.BooleanField(default='')
    on_funamation = models.BooleanField(default='')
    added_by = models.ForeignKey(
        get_user_model(), 
        on_delete=models.SET('User Deleted'), 
    )
    last_updated = models.DateTimeField(auto_now_add=True)
    
    def updated(self):
        self.last_updated = timezone.now()
        self.save()

    def __str__(self):
        return str(self.anime_name)
    
    def get_absolute_url(self):
        return reverse('anime_detail', args=[str(self.id)])
    
class Review(models.Model):
    anime_name = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def get_absolute_url(self):
        return reverse('review_list')

    def __str__(self):
        return self.review or ''
