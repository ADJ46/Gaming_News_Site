# Generated by Django 3.2.7 on 2021-09-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]