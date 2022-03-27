from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    
    #userAdim => configuration field
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Men Verdiyim Role',
            {
                'fields':(
                    'is_director',
                    'is_producer',
                )
            }
        )
    )

admin.site.register(CustomUser,CustomUserAdmin)

