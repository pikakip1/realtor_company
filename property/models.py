from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    owner_pure_phone = PhoneNumberField(region='RU', blank=True, verbose_name='Нормализованный номер владельца')
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    new_building = models.BooleanField(verbose_name='Новостройка')

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    likes = models.ManyToManyField(User, related_name='liked_flats', blank=True, verbose_name='Лайкнули')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Owner(models.Model):
    owner_name = models.CharField(max_length=50, db_index=True, verbose_name='ФИО владельца')
    owner_phone_number = models.CharField(max_length=20, db_index=True, verbose_name='Номер владельца')
    owner_pure_phone = PhoneNumberField(region='RU', db_index=True, blank=True, verbose_name='Нормализованный номер владельца')
    owner_flat = models.ManyToManyField(Flat, related_name='flat')

    def __str__(self):
        return self.owner_name


class Complaint(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто жаловался')
    apartment = models.ForeignKey(Flat, on_delete=models.CASCADE, verbose_name='На квартиру')
    text_complaint = models.TextField(max_length=1000, verbose_name='Текст жалобы')
