# Generated by Django 3.2.4 on 2021-07-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_auto_20210709_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carcolor',
            name='name',
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(default='#C0C0C0', max_length=10, verbose_name='car.CarColor'),
        ),
    ]