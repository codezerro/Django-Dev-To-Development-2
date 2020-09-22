from django.shortcuts import render
# fromm django.http import h
# Create your views here.


def basmoti_home(request):
    return render(request, 'basmoti/index.html')
