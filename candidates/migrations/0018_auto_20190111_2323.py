# Generated by Django 2.1.5 on 2019-01-11 23:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0017_auto_20190111_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=200)),
                ('last', models.CharField(max_length=200)),
                ('cover_image_url', models.URLField(blank=True, null=True)),
                ('image_urls', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, null=True, size=None)),
                ('candidate_area_type', models.CharField(choices=[('State', 'State'), ('National', 'National'), ('Other', 'Other'), ('None', 'None')], default='None', max_length=10)),
                ('last_edited', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='newcandidate',
            name='elections',
        ),
        migrations.RemoveField(
            model_name='newelection',
            name='candidates',
        ),
        migrations.RemoveField(
            model_name='newsection',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='NewCandidate',
        ),
        migrations.DeleteModel(
            name='NewElection',
        ),
        migrations.DeleteModel(
            name='NewSection',
        ),
    ]