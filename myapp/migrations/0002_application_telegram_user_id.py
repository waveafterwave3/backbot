# Generated by Django 4.1.7 on 2023-11-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='telegram_user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
