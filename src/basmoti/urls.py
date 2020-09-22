from django.urls import path
from basmoti.views import (basmoti_home)
app_name = "basmoti"

urlpatterns = [
    path('', basmoti_home, name="b_home")
]
