# Generated by Django 4.1.1 on 2022-12-05 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_post_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='banner',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, help_text='A photo to be submitted.', null=True, upload_to=''),
        ),
    ]
