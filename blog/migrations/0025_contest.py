# Generated by Django 4.1.1 on 2022-12-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(upload_to='')),
                ('submitted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-submitted'],
            },
        ),
    ]
