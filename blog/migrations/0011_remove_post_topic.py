# Generated by Django 4.1.1 on 2022-10-23 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_name_post_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
    ]
