from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class WalkMyDogUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email','city',)}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'is_dog_walker', 'is_dog_owner', 'groups', 'user_permissions',),
        }),
        ('Important dates', {'fields': ('last_login', 'date_created',)}),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    readonly_fields = ('date_created','is_dog_owner', 'is_dog_walker',)
