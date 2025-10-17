from django.shortcuts import render


def index(request):
    return render(request, "tp3/index.html")