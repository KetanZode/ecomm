# Generated by Django 4.2.3 on 2023-07-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='ccount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
