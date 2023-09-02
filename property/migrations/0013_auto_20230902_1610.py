# Generated by Django 3.2 on 2023-09-02 11:11

from django.db import migrations


def set_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for apartment in Flat.objects.all():
        flat, created = Owner.objects.get_or_create(
            owner_name=apartment.owner,
            owner_phone_number=apartment.owners_phonenumber,
            owner_pure_phone=apartment.owner_pure_phone
        )
        flat.owner_flat.add(apartment)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20230902_1610'),
    ]

    operations = [
        migrations.RunPython(set_owner_pure_phone)
    ]