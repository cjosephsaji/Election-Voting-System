# Generated by Django 5.0.7 on 2024-09-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campaign', '0006_remove_candidate_division_remove_candidate_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='division',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='candidate',
            name='grade',
            field=models.CharField(choices=[('XII', 'XII'), ('XI', 'XI'), ('X', 'X'), ('IX', 'IX'), ('VIII', 'VIII'), ('VII', 'VII'), ('VI', 'VI'), ('V', 'V'), ('IV', 'IV'), ('III', 'III'), ('II', 'II'), ('I', 'I')], default=None, max_length=4),
        ),
    ]
