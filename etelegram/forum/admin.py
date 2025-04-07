from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(DislikePost)
admin.site.register(Comment)
admin.site.register(LikeComment)
admin.site.register(DislikeComment)