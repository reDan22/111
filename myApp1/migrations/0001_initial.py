# Generated by Django 5.1.5 on 2025-05-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info', models.EmailField(max_length=254)),
                ('all_info', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
    ]
