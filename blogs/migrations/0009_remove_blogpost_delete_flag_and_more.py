# Generated by Django 4.1 on 2022-10-08 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_blogpost_delete_flag_comment_delete_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='delete_flag',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='delete_flag',
        ),
    ]
