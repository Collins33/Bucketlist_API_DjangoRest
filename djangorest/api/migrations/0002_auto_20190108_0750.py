# Generated by Django 2.1.5 on 2019-01-08 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bucketlist',
            old_name='data_modified',
            new_name='date_modified',
        ),
    ]