from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500_view(request):
    return render(request, '500.html')
