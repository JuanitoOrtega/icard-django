# Generated by Django 4.0.3 on 2022-04-12 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
    ]
