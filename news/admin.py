from django.contrib import admin
from .models import New

# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','list_date')

admin.site.register(New, NewAdmin)