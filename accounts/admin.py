from django.contrib import admin
from .models import User, OptCode
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group

@admin.register(OptCode)
class OptCodeAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "code", "created")
    readonly_fields = ('created',)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("email", "phone_number", "is_staff", "date_joined")
    list_filter = ("is_staff",)

    fieldsets = (
        ("Main", {"fields": ("email", "phone_number", "username", "password"),}),
        ("Permissions",{"fields": ("is_active", "is_staff", 'is_superuser', "last_login", 'groups', 'user_permissions'),}),
    )

    add_fieldsets = (
            ("Add User",{"fields": ("email", "phone_number", "username", "password1", "password2", "is_staff",),}),
        )

    search_fields = ("phone_number","email", "username")
    ordering = ("email",)
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj = ..., change = ..., **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form