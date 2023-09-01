from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['address', 'town']
    readonly_fields = ['created_at']
    list_display = ['town', 'address', 'price', 'owners_phonenumber', 'new_building', 'construction_year']
    list_editable = ['new_building']


admin.site.register(Flat, FlatAdmin)
