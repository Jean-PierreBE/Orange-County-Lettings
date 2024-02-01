from django.shortcuts import render
import logging
from datetime import datetime


def home(request):
    LOG_FILENAME = datetime.now().strftime('log/logfile_%d_%m_%Y.log')
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename=LOG_FILENAME, filemode='w')
    logging.info('home page url')
    return render(request, 'home.html')


def error_404_view(request, exception):
    logging.error('Error 404')
    return render(request, 'error/404.html')


def error_500_view(request):
    logging.error('Error 505')
    return render(request, 'error/500.html')
