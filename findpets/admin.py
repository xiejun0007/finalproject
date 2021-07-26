from django.contrib import admin
from .models import Findpets

# Register your models here.
class FindpetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','categories')

admin.site.register(Findpets, FindpetsAdmin)