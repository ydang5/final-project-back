# Generated by Django 2.2.6 on 2019-12-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0005_auto_20191203_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='llistudentdata',
            name='was_immigration_status_valid_date_dealt',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]