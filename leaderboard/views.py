# leaderboard/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
import requests

def fetch_leetcode_stats(username):
    try:
        url = f"https://leetcode-stats-api.herokuapp.com/{username}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else {}
    except:
        return {}

@login_required
def leaderboard_view(request):
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
    return render(request, 'leaderboard/leaderboard.html', {'user_stats': user_stats})
