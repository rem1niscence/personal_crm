# Generated by Django 2.2.6 on 2019-10-03 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0008_mood_hightlights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='hightlights',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
