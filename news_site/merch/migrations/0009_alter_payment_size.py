# Generated by Django 3.2.7 on 2021-10-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0008_alter_payment_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='size',
            field=models.IntegerField(default=32, null=True),
        ),
    ]
