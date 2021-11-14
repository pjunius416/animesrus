from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
def ChangePassword(request):
    if request.method == 'POST':
        form_class = PasswordChangeForm(request.user, request.POST)
        if form_class.is_valid():
            user = form_class.save()
            update_session_auth_hash(request, user)
            return render(request, 'registration/password_change_complete.html')
        else:
            messages.error(request, 'Password Change Failed')
    else:
        form_class = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change.html', {'form': form_class})
