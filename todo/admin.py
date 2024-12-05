from django.contrib import admin
from .models import ToDo, Tag

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'timestamp')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
