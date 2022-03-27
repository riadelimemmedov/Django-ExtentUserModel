from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
# Create your views here.

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'users/password-change.html'
    success_url = reverse_lazy('users:change-password-done')
    

class MyPasswordDoneView(PasswordResetDoneView):
    template_name = 'users/password-done.html'
    