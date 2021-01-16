from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ('css/prism.css',)
        }
        js = ('main.js','js/prism.js',)
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')