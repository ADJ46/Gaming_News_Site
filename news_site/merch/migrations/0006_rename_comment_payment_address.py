# Generated by Django 3.2.7 on 2021-10-20 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0005_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='comment',
            new_name='address',
        ),
    ]