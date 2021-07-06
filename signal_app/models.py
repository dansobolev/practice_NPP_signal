from django.db import models

from .enums import TypeEnum


class Assembly(models.Model):
    decimal_number = models.CharField(max_length=50, null=True, help_text='Децимальный номер')
    name = models.CharField(max_length=100, help_text='Наименование')
    entry_number = models.CharField(max_length=100, help_text='Входимость')

    class Meta:
        permissions = [
            "change_assembly", "User have permission to edit",
            "view_assembly", "User has permission to view",
        ]

    def __str__(self):
        return f'Сборка: {self.decimal_number}, Наименование: {self.name}, Входимость: {self.entry_number}'


class BaseProduct(models.Model):
    decimal_number = models.CharField(max_length=50, help_text='Децимальный номер', null=True)
    name = models.CharField(max_length=500, help_text='Наименование')
    entry_number = models.CharField(max_length=100, help_text='Первичная входимость', null=True)
    count_number = models.CharField(max_length=200, help_text='Количество')
    product_type = models.IntegerField(choices=TypeEnum.choices(), help_text='Тип изделия')

    class Meta:
        permissions = [
            "change_baseproduct", "User have permission to edit",
            "view_baseproduct", "User has permission to view",
        ]

    def __str__(self):
        return f'Изделие типа: {TypeEnum(self.product_type).name.title()}, первичная входимость: {self.entry_number}'
