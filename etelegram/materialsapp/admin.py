from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'material_type', 'uploaded_at')
    list_filter = ('uploaded_at', 'material_type')
    search_fields = ('title', 'description')
