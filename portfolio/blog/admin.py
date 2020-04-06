from django.contrib import admin
from blog.models import Post, View

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"title_slug" : ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(View)
