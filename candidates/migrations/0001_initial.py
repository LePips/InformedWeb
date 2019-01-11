# Generated by Django 2.1.5 on 2019-01-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewCandidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('canidate_area_type', models.CharField(choices=[('state', 'State'), ('national', 'National'), ('other', 'Other'), ('none', '')], default='none', max_length=2)),
                ('last_edited', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewElection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='newcandidate',
            name='elections',
            field=models.ManyToManyField(to='candidates.NewElection'),
        ),
    ]
