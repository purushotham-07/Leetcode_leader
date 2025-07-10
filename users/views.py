from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
import requests

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def fetch_leetcode_stats(username):
    try:
        url = f"https://leetcode-stats-api.herokuapp.com/{username}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else {}
    except:
        return {}

@login_required
def dashboard_view(request):
    users = CustomUser.objects.all()
    user_stats = []
    for user in users:
        stats = fetch_leetcode_stats(user.leetcode_id)
        user_stats.append({
            'user': user,
            'totalSolved': stats.get('totalSolved', 0),
            'easySolved': stats.get('easySolved', 0),
            'mediumSolved': stats.get('mediumSolved', 0),
            'hardSolved': stats.get('hardSolved', 0),
        })
    user_stats.sort(key=lambda x: x['totalSolved'], reverse=True)
    return render(request, 'users/dashboard.html', {'user_stats': user_stats})
