import logging
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting


def index(request):
    """return the list of lettings """
    logging.info('page of lettings')
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """ """
    text_log = 'letting id : {id}'.format(id=letting_id)
    logging.info(text_log)
    letting_extr = get_object_or_404(Letting, pk=letting_id)
    context = {
        'title': letting_extr.title,
        'address': letting_extr.address,
    }
    return render(request, 'lettings/letting.html', context)
