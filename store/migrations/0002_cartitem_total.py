# Generated by Django 4.2 on 2023-04-26 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]