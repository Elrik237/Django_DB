# Generated by Django 3.2 on 2021-04-27 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0002_auto_20210427_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clickstatistics',
            options={'verbose_name': 'Статистика действий пользователей', 'verbose_name_plural': 'Статистика действий пользователей'},
        ),
        migrations.AlterModelOptions(
            name='userrequests',
            options={'verbose_name': 'Список уникальных пользователей', 'verbose_name_plural': 'Список уникальных пользователей'},
        ),
    ]
