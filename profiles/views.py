""" views for profile app """
import logging
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


def index(request):
    """ list of profiles """
    logging.info('page of profiles')
    profiles_list = Profile.objects.all()               # pylint: disable=E1101
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """ detail for one profile """
    id_user = username
    text_log = f"profile username : {id_user} "
    logging.info(text_log)
    profile_extr = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile_extr}
    return render(request, 'profiles/profile.html', context)
