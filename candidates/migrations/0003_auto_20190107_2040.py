# Generated by Django 2.1.5 on 2019-01-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_auto_20190107_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcandidate',
            name='candidate_area_type',
            field=models.CharField(choices=[('State', 'State'), ('National', 'National'), ('Other', 'Other'), ('None', 'None')], default='no', max_length=10),
        ),
    ]
