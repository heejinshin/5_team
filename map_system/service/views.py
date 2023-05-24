from django.shortcuts import render


def index(request):
    return render(request, 'choosebar.html')

def show_map(request):
    return render(request, 'map.html')

