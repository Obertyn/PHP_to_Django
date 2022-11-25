from django.contrib import admin
from .models import Users
# Register your models here.

#admin.site.register(Users)
@admin.register(Users)

class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id_user',
        'user',
        'password',
        'email',
        'wood',
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'user',
        'email',
    )
    ordering = (
        'user',
        'wood',
    )

