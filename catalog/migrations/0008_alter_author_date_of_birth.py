# Generated by Django 3.2.17 on 2023-02-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_author_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
