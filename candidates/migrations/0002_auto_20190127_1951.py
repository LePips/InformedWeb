# Generated by Django 2.1.5 on 2019-01-27 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='other_party',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.CharField(choices=[('Democrat', 'Democrat'), ('Republican', 'Republican'), ('Independent', 'Independent'), ('Other', 'Other'), ('None', 'None')], default='None', max_length=15),
        ),
    ]
