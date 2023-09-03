from django.contrib import admin
from .models import Flat, Complaint, Owner


class PropertyOwnersInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('owner', 'flat')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['address', 'town']
    readonly_fields = ['created_at']
    list_display = ['town', 'address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('likes',)

    inlines = [PropertyOwnersInline]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

    inlines = [PropertyOwnersInline]
    exclude = ['flat']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('name', 'apartment')
