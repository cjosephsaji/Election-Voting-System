# Generated by Django 5.0.7 on 2024-09-28 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0007_candidate_division_candidate_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='division',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='grade',
        ),
    ]
