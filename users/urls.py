from django.urls import path
from .views import signup_view, login_view, logout_view, dashboard_view

urlpatterns = [
    path('', login_view, name='home'),               # Optional: root redirects to login
    path('login/', login_view, name='login'),        # ✅ Add this for explicit login route
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
