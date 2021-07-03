# Generated by Django 3.2.5 on 2021-07-03 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Децимальный номер', max_length=50, null=True)),
                ('name', models.CharField(help_text='Наименование', max_length=100)),
                ('entry_number', models.CharField(help_text='Входимость', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StandardProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Наименование', max_length=500)),
                ('count_number', models.CharField(help_text='Количество', max_length=200)),
                ('entry_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signal_app.assembly')),
            ],
        ),
        migrations.CreateModel(
            name='OtherProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Наименование', max_length=500)),
                ('count_number', models.CharField(help_text='Количество', max_length=200)),
                ('entry_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signal_app.assembly')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Децимальный номер', max_length=50)),
                ('name', models.CharField(help_text='Наименование', max_length=500)),
                ('count_number', models.CharField(help_text='Количество', max_length=200)),
                ('entry_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signal_app.assembly')),
            ],
        ),
    ]