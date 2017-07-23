# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Summary,User,EnergyUse

# Register your models here.

admin.site.register(Summary)
admin.site.register(User)
admin.site.register(EnergyUse)
