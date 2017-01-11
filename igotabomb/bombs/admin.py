from django.contrib import admin
from .models import BombType


class BombTypeAdmin(admin.ModelAdmin):
    model = BombType
    list_display = ('__unicode__', 'duration', 'brange', )
    fields = ('name', 'duration', 'duration_starting',
              'duration_ending', 'brange', 'image', 'user_change_location',
              'change_location', 'stealth', 'simultaneous', )
    readonly_fields = ('duration', )

    def duration(self, obj):
        return obj.duration


admin.site.register(BombType, BombTypeAdmin)
