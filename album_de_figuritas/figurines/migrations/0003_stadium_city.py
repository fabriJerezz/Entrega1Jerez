# Generated by Django 4.1.2 on 2022-11-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figurines', '0002_rename_nacionalteam_nationalteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium',
            name='city',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]