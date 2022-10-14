from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required

def index(request):
    users = get_user_model().objects.all()
    context={
        'users':users
    }
    return render(request, 'accounts/index.html',context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def detail(request, user_pk):
    user = get_user_model().objects.get(id=user_pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

@login_required
def update(request, user_pk):
    if request.method == 'POST':
        if request.user.pk == user_pk:
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('accounts:detail', request.user.pk)
        else:
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/password.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')
