# Generated by Django 4.1 on 2022-10-19 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0018_comment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parent',
            new_name='reply',
        ),
    ]
