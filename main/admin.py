from django.contrib import admin
from .models import *


@admin.register(RoomModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']


admin.site.register(TopicModel)
admin.site.register(MessageModel)
