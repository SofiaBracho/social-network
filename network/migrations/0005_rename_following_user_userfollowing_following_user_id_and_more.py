# Generated by Django 4.2.5 on 2024-01-11 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_rename_following_user_id_userfollowing_following_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfollowing',
            old_name='following_user',
            new_name='following_user_id',
        ),
        migrations.RenameField(
            model_name='userfollowing',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('user_id', 'following_user_id')},
        ),
    ]
