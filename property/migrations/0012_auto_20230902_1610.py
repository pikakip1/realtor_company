# Generated by Django 3.2 on 2023-09-02 13:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20230902_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_phone_number',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region='RU', verbose_name='Нормализованный номер владельца'),
        ),
    ]
