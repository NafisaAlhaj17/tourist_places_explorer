from django.contrib import admin
from .models import Place, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'state', 'category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'city', 'state')
    list_filter = ('category', 'city')
