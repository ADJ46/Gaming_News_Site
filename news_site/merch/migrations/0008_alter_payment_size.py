# Generated by Django 3.2.7 on 2021-10-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0007_auto_20211021_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='size',
            field=models.CharField(max_length=255),
        ),
    ]
