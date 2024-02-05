import logging
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


def index(request):
    logging.info('page of profiles')
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    text_log = 'profile username : {id}'.format(id=username)
    logging.info(text_log)
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
