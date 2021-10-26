from django.contrib import admin
from . models import *

# Register your models here.

# admin.site.register(Akta)

@admin.register(Akta)
class AktaAdmin(admin.ModelAdmin):
    list_display = ('user', 'nama_anak')