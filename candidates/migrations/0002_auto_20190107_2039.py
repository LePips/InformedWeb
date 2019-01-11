# Generated by Django 2.1.5 on 2019-01-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newcandidate',
            name='canidate_area_type',
        ),
        migrations.AddField(
            model_name='newcandidate',
            name='candidate_area_type',
            field=models.CharField(choices=[('st', 'State'), ('nl', 'National'), ('ot', 'Other'), ('no', '')], default='no', max_length=2),
        ),
    ]
