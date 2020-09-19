from django.urls import include, path
from pages.views import (index, about)

app_name = "pages"

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about")
]
