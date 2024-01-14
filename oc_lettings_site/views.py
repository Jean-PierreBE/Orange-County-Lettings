from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def error_404_view(request, exception):
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')


def error_500_view(request):
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '500.html')

