# Generated by Django 5.1 on 2024-08-31 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher',
            new_name='publishere',
        ),
        migrations.AlterField(
            model_name='book',
            name='pubdate',
            field=models.DateField(default=datetime.datetime(2024, 8, 31, 21, 36, 4, 794838)),
        ),
    ]
