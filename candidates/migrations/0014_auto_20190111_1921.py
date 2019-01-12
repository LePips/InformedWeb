# Generated by Django 2.1.5 on 2019-01-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0013_auto_20190111_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='newelection',
            name='election_area_type',
            field=models.CharField(choices=[('State', 'State'), ('National', 'National'), ('None', 'None')], default='None', max_length=10),
        ),
        migrations.AddField(
            model_name='newelection',
            name='last_edited',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='newcandidate',
            name='candidate_area_type',
            field=models.CharField(choices=[('State', 'State'), ('National', 'National'), ('Other', 'Other'), ('None', 'None')], default='None', max_length=10),
        ),
    ]