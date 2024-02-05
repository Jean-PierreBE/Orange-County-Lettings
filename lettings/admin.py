""" put model Letting and Address in Administration """
from django.contrib import admin
from lettings.models import Letting, Address

admin.site.register(Letting)
admin.site.register(Address)
