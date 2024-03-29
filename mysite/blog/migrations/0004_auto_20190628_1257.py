# Generated by Django 2.2 on 2019-06-28 07:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190628_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approve_comment',
            new_name='approved_comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 7, 27, 24, 374398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 7, 27, 24, 374398, tzinfo=utc)),
        ),
    ]
