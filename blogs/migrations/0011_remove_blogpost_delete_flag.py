# Generated by Django 4.1 on 2022-10-08 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_blogpost_delete_flag_comment_delete_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='delete_flag',
        ),
    ]
