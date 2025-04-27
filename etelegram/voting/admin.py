from django.contrib import admin
from .models import *
admin.site.register(Voting)
admin.site.register(Session)
admin.site.register(UserAnswer)
admin.site.register(Answer)
