
# Generated by Django 3.1.6 on 2021-02-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lgu', '0002_addcoordinates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localgovernmentunit',
            name='registrant_map',
            field=models.FileField(blank=True, null=True, upload_to='static/maps/'),
        ),
    ]
