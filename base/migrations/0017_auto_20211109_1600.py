# Generated by Django 3.2.6 on 2021-11-09 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_boards_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='boards',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='base.boards'),
            preserve_default=False,
        ),
    ]