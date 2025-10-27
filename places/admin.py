from django.contrib import admin
from .models import Place, Category, Feedback

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'state', 'category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'city', 'state')
    list_filter = ('category', 'city')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'rating', 'approved', 'created_at')
    list_filter = ('approved', 'rating', 'created_at')
    search_fields = ('name', 'email', 'comment')
    list_editable = ('approved',)
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Visitor Information', {
            'fields': ('name', 'email')
        }),
        ('Feedback Details', {
            'fields': ('place', 'rating', 'comment')
        }),
        ('Moderation', {
            'fields': ('approved', 'created_at')
        }),
    )
