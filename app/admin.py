from django.contrib import admin
from .models import Room, RequestFormModel, NotificationBox

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'user')

@admin.register(RequestFormModel)
class RequestFormModelAdmin(admin.ModelAdmin):
    list_display = ('titel', 'is_universal')
    filter_horizontal = ('user',)  # Allows easier selection of multiple users in admin

@admin.register(NotificationBox)
class NotificationBoxAdmin(admin.ModelAdmin):
    list_display = ('room', 'title', 'type_msg', 'created_at')
    list_filter = ('type_msg', 'created_at')
