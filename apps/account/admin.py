from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Account, AccountUser
from .forms import AccountUserChangeForm, AccountUserCreationForm


class AccountUserAdmin(UserAdmin):
    """ Forms to add and change Users
    Remove 'username' field as 'email' is our only login field
    """
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('User info'), {'fields': ('first_name', 'last_name', 'account',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_created')}),
    )
    form = AccountUserChangeForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    add_form = AccountUserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'last_login',)
    search_fields = ('email', 'first_name', 'last_name',)
    readonly_fields = ('date_created', 'last_login', 'account',)
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        # New users will be attached to same account as their creator
        obj.account = request.user.account
        super(AccountUserAdmin, self).save_model(request, obj, form, change)


admin.site.register(AccountUser, AccountUserAdmin)
admin.site.register(Account)
