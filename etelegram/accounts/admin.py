from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin as DefaultGroupAdmin
from .models import CustomUser

class GroupAdmin(DefaultGroupAdmin):
    list_display = ('name', 'user_count', 'user_list')
    readonly_fields = ('user_list',)

    def user_count(self, obj):
        return obj.customuser_groups.count()
    user_count.short_description = 'Кількість користувачів'

    def user_list(self, obj):
        users = obj.customuser_groups.all()
        if users.exists():
            return ", ".join([user.username for user in users])
        return "—"
    user_list.short_description = 'Користувачі в групі'

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(CustomUser)
