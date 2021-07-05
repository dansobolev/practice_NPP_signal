from django.db import models

from .enums import TypeEnum


class Assembly(models.Model):
    decimal_number = models.CharField(max_length=50, null=True, help_text='Децимальный номер')
    name = models.CharField(max_length=100, help_text='Наименование')
    entry_number = models.CharField(max_length=100, help_text='Входимость')

    def __str__(self):
        return f'Сборка: {self.decimal_number}, {self.name}, {self.entry_number}'


class BaseProduct(models.Model):
    decimal_number = models.CharField(max_length=50, help_text='Децимальный номер', null=True)
    name = models.CharField(max_length=500, help_text='Наименование')
    entry_number = models.CharField(max_length=100, help_text='Первичная входимость', null=True)
    count_number = models.CharField(max_length=200, help_text='Количество')
    product_type = models.IntegerField(choices=TypeEnum.choices(), help_text='Тип изделия')

    def __str__(self):
        return f'Изделие типа: {self.product_type}, первичная входимость: {self.entry_number}'
