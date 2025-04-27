from django.contrib import admin

from .models import Portfolio, Portfolio_like, Portfolio_dislike


admin.site.register(Portfolio)
admin.site.register(Portfolio_like)
admin.site.register(Portfolio_dislike)


