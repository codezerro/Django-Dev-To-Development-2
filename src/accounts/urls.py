from django.urls import path
from .views import (login, register, logout, dashboard)
app_name = "accounts"
urlpatterns = [
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('dashboard', dashboard, name="dashboard"),
    path('logout', logout, name="logout")
]
