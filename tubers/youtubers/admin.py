from django.contrib import admin
from django.utils.html import format_html
from .models import Youtuber

# Register your models here.

class Ytadmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html("<img src={} width=40 />".format(object.photo.url))

    list_display = ('id', 'name', 'myphoto', 'subs_count', 'is_featured')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'camera_type')
    list_filter = ('category', 'camera_type')
    list_editable = ('is_featured',)

admin.site.register(Youtuber, Ytadmin)
