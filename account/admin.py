from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('phone', 'date_joined', 'last_login', 'is_admin', 'is_staff',)
    search_fields = ('phone',)
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('phone',)


admin.site.register(Account, AccountAdmin)