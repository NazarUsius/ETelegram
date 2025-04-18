from django.contrib import admin
from .models import *

admin.site.register(Quiz)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Answer)