# Generated by Django 5.0.7 on 2024-10-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0005_remove_student_list_division_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_list',
            name='voted',
            field=models.BooleanField(default=False),
        ),
    ]