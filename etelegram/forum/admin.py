from django.contrib import admin
from .models import *

admin.site.register(Branch)
admin.site.register(LikeBranch)
admin.site.register(DislikeBranch)
admin.site.register(Comment)
admin.site.register(LikeComment)
admin.site.register(DislikeComment)