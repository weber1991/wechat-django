# -*- coding:utf-8 -*-
from django.contrib import admin
from datashow.models import Screlation
# Register your models here.
class ScrelationAadmin(admin.ModelAdmin):
    ordering = ("serviceid",)

admin.site.register(Screlation, ScrelationAadmin)