from django.contrib import admin
from .models import Findpeople

# Register your models here.
class FindpeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Findpeople, FindpeopleAdmin)