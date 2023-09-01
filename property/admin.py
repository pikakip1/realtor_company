from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['address', 'town']
    readonly_fields = ['created_at']
    list_display = ['town', 'address', 'price', 'owners_phonenumber', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('name', 'apartment')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
