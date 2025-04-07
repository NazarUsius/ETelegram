from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin as DefaultGroupAdmin

class GroupAdmin(DefaultGroupAdmin):
    list_display = ('name', 'user_count', 'user_list')
    readonly_fields = ('user_list',)

    def user_count(self, obj):
        return obj.user_set.count()
    user_count.short_description = 'Кількість користувачів'

    def user_list(self, obj):
        users = obj.user_set.all()
        if users.exists():
            return ", ".join([user.username for user in users])
        return "—"
    user_list.short_description = 'Користувачі в групі'

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
