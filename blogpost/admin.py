from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['description']}),
        ('Date Information', {'fields': ['created_at'], 'classes': ['collapse']}),
    ]
    # inlines = [ChoiceInline]
    list_display = ('title', 'created_at', 'was_published_recently')
    list_filter = ['created_at']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)