# Generated by Django 3.2 on 2023-09-02 09:46

from django.db import migrations


def set_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for apartment in Flat.objects.all():
        Owner.objects.get_or_create(
            owner_name=apartment.owner, owner_phone_number=apartment.owners_phonenumber,
            defaults={
                'owner_pure_phone': apartment.owner_pure_phone,
            }
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(set_owners)
    ]