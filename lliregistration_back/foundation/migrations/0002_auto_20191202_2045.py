# Generated by Django 2.2.6 on 2019-12-02 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='llistudentmastersheetupload',
            options={'default_permissions': (), 'permissions': (), 'verbose_name': 'LLI Student Master Sheet File Upload', 'verbose_name_plural': 'LLI Student Master Sheet Uploads'},
        ),
        migrations.AlterModelTable(
            name='llistudentmastersheetupload',
            table='lli_student_master_sheet_file_uploads',
        ),
    ]