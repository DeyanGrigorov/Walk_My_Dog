from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class WalkMyDogUserAdmin(UserAdmin):
    readonly_fields = ('date_created', 'first_name', 'last_name', 'city',)
    list_display = ('email', 'is_staff', 'category')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'city', 'category')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions',),
        }),
        ('Important dates', {'fields': ('last_login', 'date_created',)}),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'category', 'city', 'password1', 'password2'),
        }),
    )
