# Generated by Django 5.0.7 on 2024-10-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0013_candidate_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]