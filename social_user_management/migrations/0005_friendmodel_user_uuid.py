# Generated by Django 5.0.6 on 2024-06-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_user_management', '0004_alter_friendmodel_friend_acceptance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendmodel',
            name='user_uuid',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
