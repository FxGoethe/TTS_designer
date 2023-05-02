from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "TTS_designer"

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('cName','cID','cCost','cEffect','cStory','image_data')
    ordering = ('cID',)

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('Fdiscription','FField')