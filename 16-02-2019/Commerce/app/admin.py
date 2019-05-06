from django.contrib import admin
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js
from .models import *
class productmodel(admin.ModelAdmin):
    list_display = ["name","image","publication_status","price"]
    list_display_links = ["name"]
    list_filter = ["publication_status"]
    search_fields = ["name","price"]
    class Meta:
        model=product
admin.site.register(category)
admin.site.register(Manufactuar)
admin.site.register(product)

# Register your models here.
