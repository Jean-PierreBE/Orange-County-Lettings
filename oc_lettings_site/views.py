""" views for the project"""
import logging
from datetime import datetime
from django.shortcuts import render


def home(request):
    """ view for the home page"""
    log_filename = datetime.now().strftime('log/logfile_%d_%m_%Y.log')
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO,
                        filename=log_filename, filemode='w')
    logging.info('home page url')
    return render(request, 'home.html')


def error_404_view(request, exception):   # pylint: disable=W0613
    """ return a personal page 404 if error"""
    logging.error('Error 404')
    return render(request, 'error/404.html')


def error_500_view(request):
    """ return a personal page 500 if error"""
    logging.error('Error 505')
    return render(request, 'error/500.html')
