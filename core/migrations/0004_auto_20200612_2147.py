# Generated by Django 3.0.6 on 2020-06-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200610_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[('Buyer', 'Buyer'), ('Manager', 'Manager')], max_length=200, null=True),
        ),
    ]