# Generated by Django 4.1 on 2022-10-19 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0019_rename_parent_comment_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reply',
            new_name='parent',
        ),
    ]
