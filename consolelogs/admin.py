from django.contrib import admin

from . import models


class ConsoleLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', )


admin.site.register(models.ConsoleLog)
