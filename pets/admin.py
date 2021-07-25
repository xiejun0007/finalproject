from django.contrib import admin
from .models import Pets

# Register your models here.
class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Pets, PetsAdmin)