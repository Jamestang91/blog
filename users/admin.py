from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# username:Kaycool123 password:kay123456789
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'country', 'occupation', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'country', 'occupation',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'age', 'country', 'occupation',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
