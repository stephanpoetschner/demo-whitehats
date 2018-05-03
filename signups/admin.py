from django.contrib import admin

from .models import SignupUser


class SignupUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'created', )


admin.site.register(SignupUser, SignupUserAdmin)
