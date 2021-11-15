from django.urls import path
from . import views
from .views import (AnimeListView, AnimeUpdateView, AnimeDetailView, AnimeDeleteView, AnimeCreateView, 
                    ReviewListView, ReviewCreateView, ReviewDeleteView, ReviewUpdateView)

urlpatterns = [
    path('<int:pk>/edit/', AnimeUpdateView.as_view(), name='anime_edit'),
    path('<int:pk>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('<int:pk>/delete/', AnimeDeleteView.as_view(), name='anime_delete'),
    path('new/', AnimeCreateView.as_view(), name='anime_new'),
    path('', AnimeListView.as_view(), name='anime_list'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/new/', ReviewCreateView.as_view(), name='review_new'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('reviews/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
    path('requestdelete/', views.request_anime_delete, name='request_delete'),
    path('requestdelete/success', views.deletion_request_sent, name='request_sent'),
    
]
