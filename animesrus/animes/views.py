from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Anime
from django.urls import reverse_lazy

class AnimeListView(ListView):
    model = Anime
    template_name = 'anime_list.html'

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime_detail.html'

class AnimeUpdateView(UpdateView):
    model = Anime
    fields = ('anime_name', 'wiki_url', 'description', 'language_type', 'on_hulu', 'on_netflix', 'on_crunchyroll', 'on_funamation')
    template_name = 'anime_edit.html'

class AnimeDeleteView(DeleteView):
    model = Anime
    template_name = 'anime_delete.html'
    success_url = reverse_lazy('anime_list')
    
class AnimeCreateView(CreateView):
    model = Anime
    template_name = 'anime_new.html'
    fields = ('anime_name', 'wiki_url', 'description', 'language_type', 'on_hulu', 'on_netflix', 'on_crunchyroll', 'on_funamation')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
