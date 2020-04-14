from django.contrib import admin
from .models import Players, Organizations, ChatMessages


# Register your models here.

admin.site.register(Players)
admin.site.register(Organizations)
admin.site.register(ChatMessages)