# Generated by Django 4.2.5 on 2023-10-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registered_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Passwd', models.CharField(max_length=20)),
                ('Userbirthday', models.DateField()),
                ('Usermail', models.EmailField(blank=True, default='', max_length=100)),
                ('Usertel', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
