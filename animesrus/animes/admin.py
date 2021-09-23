from django.contrib import admin

from .models import Anime, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ( 'review', 'anime_name', 'author' )

class ReviewInLine(admin.TabularInline):
    model = Review
    
class AnimeAdmin(admin.ModelAdmin):
    list_display = ( 'anime_name', 'language_type', 'on_hulu', 'on_netflix', 'on_crunchyroll', 'on_funamation', 'added_by' )
    inlines = [
        ReviewInLine,
    ]

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Review, ReviewAdmin)