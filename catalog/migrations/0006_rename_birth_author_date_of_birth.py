# Generated by Django 3.2.17 on 2023-02-03 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_date_of_birth_author_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='birth',
            new_name='date_of_birth',
        ),
    ]
