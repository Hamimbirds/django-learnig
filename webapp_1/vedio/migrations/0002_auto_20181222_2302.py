# Generated by Django 2.1a1 on 2018-12-22 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vedio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_vedio',
            old_name='embeded',
            new_name='embed_code',
        ),
    ]
