from django.db import models


class Assembly(models.Model):
    number = models.CharField(max_length=50, null=True, help_text='Децимальный номер')
    name = models.CharField(max_length=100, help_text='Наименование')
    entry_number = models.CharField(max_length=100, help_text='Входимость')

    def __str__(self) -> str:
        return f'Сборка: {self.number}, {self.name}, {self.entry_number}'


class Detail(models.Model):
    number = models.CharField(max_length=50, help_text='Децимальный номер')
    name = models.CharField(max_length=500, help_text='Наименование')
    entry_number = models.ForeignKey(Assembly, on_delete=models.CASCADE)
    count_number = models.CharField(max_length=200, help_text='Количество')


class StandardProduct(models.Model):
    number = models.CharField(max_length=50, help_text='Децимальный номер', null=True)
    name = models.CharField(max_length=500, help_text='Наименование')
    entry_number = models.ForeignKey(Assembly, on_delete=models.CASCADE)
    count_number = models.CharField(max_length=200, help_text='Количество')


class OtherProduct(models.Model):
    number = models.CharField(max_length=50, help_text='Децимальный номер', null=True)
    name = models.CharField(max_length=500, help_text='Наименование')
    entry_number = models.ForeignKey(Assembly, on_delete=models.CASCADE)
    count_number = models.CharField(max_length=200, help_text='Количество')
