from django.contrib import admin
from blog.models import Post, View, Like

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"title_slug" : ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(View)
admin.site.register(Like)
