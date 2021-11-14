from django.urls import path
from . import views
from .views import (AnimeListView, AnimeUpdateView, AnimeDetailView, AnimeDeleteView, AnimeCreateView)

urlpatterns = [
    path('<int:pk>/edit/', AnimeUpdateView.as_view(), name='anime_edit'),
    path('<int:pk>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('<int:pk>/delete/', AnimeDeleteView.as_view(), name='anime_delete'),
    path('new/', AnimeCreateView.as_view(), name='anime_new'),
    path('', AnimeListView.as_view(), name='anime_list'),

]
