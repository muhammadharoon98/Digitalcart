# Generated by Django 3.2 on 2021-04-24 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=''),
        ),
    ]