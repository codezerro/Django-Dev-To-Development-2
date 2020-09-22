from django.shortcuts import render

# Create your views here.


def imgCompress(request):
    return render(request, 'imgupload/index.html')
