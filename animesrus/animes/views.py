from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .forms import *
from .models import models
from .models import Anime, Review
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

#Review Views
class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    
class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review_new.html'
    fields = ('anime_name', 'review', 'author')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('review_list')
    
class ReviewUpdateView(UpdateView):
    model = Review
    fields = ('anime_name', 'review', 'author')
    template_name = 'review_edit.html'
    
def request_anime_delete(request):
    if request.method == 'GET':
        form = RequestDeleteForm()
    else:
        form = RequestDeleteForm(request.POST)
        if form.is_valid():
            anime_name = form.cleaned_data['anime_name']
            email_address = form.cleaned_data['email_address']
            reason = form.cleaned_data['reason_for_deletion']
            message = "Anime to be Deleted " + anime_name + "\nDeletion Requested by: " + email_address + "\nReason For Deletion: " + reason 
            try:
                send_mail(anime_name, message, email_address, ['localhost'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('request_sent')
    return render(request, 'request_delete.html', {'form': form})

def deletion_request_sent(request):
    return render(request, 'request_sent.html')