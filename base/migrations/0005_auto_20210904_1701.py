# Generated by Django 3.2.6 on 2021-09-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_comment_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='boards',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]