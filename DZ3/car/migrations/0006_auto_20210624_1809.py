# Generated by Django 3.2.4 on 2021-06-24 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20210605_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Car type',
                'verbose_name_plural': 'Car types',
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AddField(
            model_name='car',
            name='product_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CarColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.company')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.cartype'),
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.carcolor'),
        ),
    ]
