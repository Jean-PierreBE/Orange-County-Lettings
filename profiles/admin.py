""" put model Profile in Administration"""
from django.contrib import admin
from profiles.models import Profile

admin.site.register(Profile)
