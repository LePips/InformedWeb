# Generated by Django 2.1.5 on 2019-01-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0015_newelection_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newelection',
            name='cover_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]