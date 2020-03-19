from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import generic
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from .forms import SignupForm, PasswordChangeForm

class Signup(generic.CreateView):
    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/management')
        else:
            return render(request, 'management/signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = SignupForm()
        return render(request, 'management/signup.html', {'form': form})

class UserDetail(generic.CreateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = PasswordChangeForm()
            return render(request, 'management/userDetail.html', {'form': form})
        else:
            return redirect(to='/accounts/login')

class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('management:password_change_done')
    template_name = 'management/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'management/password_change_done.html'

class UserDelete(generic.CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        self.request.user.delete()
        return redirect(to='/accounts/login')

class Management(generic.CreateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = self.request.user
            return render(request, 'management/management.html')
        else:
            return redirect(to='/accounts/login')