# Generated by Django 3.2.7 on 2021-10-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0006_rename_comment_payment_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='status',
            new_name='payment_status',
        ),
        migrations.AddField(
            model_name='payment',
            name='mode',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='size',
            field=models.IntegerField(default=32),
        ),
    ]
