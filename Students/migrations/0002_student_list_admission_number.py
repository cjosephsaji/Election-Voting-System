# Generated by Django 5.0.7 on 2024-09-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_list',
            name='admission_number',
            field=models.IntegerField(default=None),
        ),
    ]