from django.contrib import admin

# Register your models here.
from app.models import *

class CustomeWebpages(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_display_links=['url']
    list_editable=('name',)
    search_fields=['name']
    list_per_page=3
    list_filter=['name']


admin.site.register(Topic)

admin.site.register(WebPage,CustomeWebpages)

admin.site.register(AccessRecord)