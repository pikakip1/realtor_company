from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['address', 'town']
    readonly_fields = ['created_at']
    list_display = ['town', 'address', 'price', 'owners_phonenumber', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']

    raw_id_fields = ('likes',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owner_flat',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('name', 'apartment')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)