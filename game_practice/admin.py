from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Platform)
'''
class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'address', 'time_ordered')
'''
admin.site.register(Game)