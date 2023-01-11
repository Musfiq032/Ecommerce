# Generated by Django 4.1.5 on 2023-01-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECommerceAuth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
