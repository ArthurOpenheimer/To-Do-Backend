from django.contrib import admin
from todo.models import Todo, User

class Todos(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class Users(admin.ModelAdmin):
    list_display = ('id', 'username')
    search_fields = ('username',)
    
admin.site.register(Todo, Todos)
admin.site.register(User, Users)

