# Generated by Django 2.1.5 on 2019-01-12 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0018_auto_20190111_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='candidate_area_type',
            new_name='type',
        ),
    ]
