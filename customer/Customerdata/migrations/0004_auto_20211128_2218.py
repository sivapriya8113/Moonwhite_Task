# Generated by Django 3.2.9 on 2021-11-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customerdata', '0003_alter_address_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='updatedon',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='updatedon',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]