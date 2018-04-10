from django.contrib import admin

# Register your models here.

from post.models import *

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)