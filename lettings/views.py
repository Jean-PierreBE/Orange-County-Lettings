""" view for the lettings """
import logging
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting


def index(request):
    """return the list of lettings """
    logging.info('page of lettings')
    lettings_list = Letting.objects.all()           # pylint: disable=E1101
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """ detail of one letting """
    id_let = letting_id
    text_log = f"letting id : {id_let} "
    logging.info(text_log)
    letting_extr = get_object_or_404(Letting, pk=letting_id)
    context = {
        'title': letting_extr.title,
        'address': letting_extr.address,
    }
    return render(request, 'lettings/letting.html', context)
