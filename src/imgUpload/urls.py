from django.urls import path
from .views import (imgCompress)

app_name = "imgupload"
urlpatterns = [
    path('', imgCompress, name="imgcompress")
]
