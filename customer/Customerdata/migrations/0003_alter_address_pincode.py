# Generated by Django 3.2.9 on 2021-11-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customerdata', '0002_alter_address_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
