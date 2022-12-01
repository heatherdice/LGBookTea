from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fields = ('name', 'username', 'email', 'password')
    list_display = ['name', 'username', 'email', 'id']
    search_fields = ['name', 'username', 'email']
    ordering = ['name', '-name', 'username', '-username', 'email', '-email', 'id', '-id'] # while in dash, can order by id in ascending & descending order

admin.site.register(User, UserAdmin)

