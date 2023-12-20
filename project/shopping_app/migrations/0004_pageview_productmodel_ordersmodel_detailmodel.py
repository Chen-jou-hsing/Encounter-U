# Generated by Django 4.2.5 on 2023-10-21 18:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0003_alter_registered_user_passwd'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=255)),
                ('total_views', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('daily_views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default='', max_length=100)),
                ('pprice', models.IntegerField(default=0)),
                ('pimages', models.CharField(default='', max_length=100)),
                ('pdescription', models.TextField(blank=True, default='')),
                ('pcategory', models.CharField(default='Uncategorized', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrdersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.IntegerField(default=0)),
                ('shipping', models.IntegerField(default=0)),
                ('grandtotal', models.IntegerField(default=0)),
                ('customname', models.CharField(default='', max_length=100)),
                ('customaddress', models.CharField(default='', max_length=100)),
                ('customphone', models.CharField(default='', max_length=100)),
                ('shipping_method', models.CharField(default='', max_length=50)),
                ('paytype', models.CharField(default='', max_length=50)),
                ('customemail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shopping_app.registered_user')),
            ],
        ),
        migrations.CreateModel(
            name='DetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default='', max_length=100)),
                ('unitprice', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('dtotal', models.IntegerField(default=0)),
                ('shipping_fee', models.FloatField(default=0.0)),
                ('dorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_app.ordersmodel')),
            ],
        ),
    ]