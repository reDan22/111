# Generated by Django 5.1.6 on 2025-05-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp1', '0006_whoisdfs'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerbuild',
            name='ssd',
            field=models.CharField(default='1024 GB', max_length=255),
        ),
    ]
