from django.contrib import admin
from . models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" wdth="40px" height="50px" style="border-radius:10px;"/>.'.format(object.photo.url))
    
    thumbnail.short_description="Photo"



    list_display=('id','firstname','thumbnail','lastname','designation','created_date')
    list_display_links=('firstname','id','thumbnail')
    search_fields=('firstname','lastname','designation')
    list_filter=('designation',)


admin.site.register(Team,TeamAdmin)