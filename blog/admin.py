from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','author')

admin.site.register(Post)
admin.site.register(Comment,CommentAdmin)

