# Generated by Django 5.1.7 on 2025-03-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0003_house_screenshot_houseimage_screenshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseimage',
            name='screenshot',
        ),
    ]
