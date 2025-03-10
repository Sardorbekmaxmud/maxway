# Generated by Django 5.1.3 on 2024-12-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_side', '0006_alter_order_address_alter_order_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
