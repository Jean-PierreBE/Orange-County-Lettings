import logging
from datetime import datetime
from django.shortcuts import render


def home(request):
    log_filename = datetime.now().strftime('log/logfile_%d_%m_%Y.log')
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO,
                        filename=log_filename, filemode='w')
    logging.info('home page url')
    return render(request, 'home.html')


def error_404_view(request, exception):
    logging.error('Error 404')
    return render(request, 'error/404.html')


def error_500_view(request):
    logging.error('Error 505')
    return render(request, 'error/500.html')
