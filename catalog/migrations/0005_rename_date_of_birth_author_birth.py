# Generated by Django 3.2.17 on 2023-02-03 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20230203_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='date_of_birth',
            new_name='birth',
        ),
    ]
