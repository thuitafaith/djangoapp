# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Editor,Article,tags 

from django.contrib import admin

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)