# Generated by Django 2.1.5 on 2019-01-26 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elections', '0001_initial'),
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateInfoRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=800)),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='infoRequests', to='candidates.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('candidates', models.ManyToManyField(blank=True, related_name='contributors', to='candidates.Candidate')),
                ('elections', models.ManyToManyField(blank=True, related_name='contributors', to='elections.Election')),
            ],
        ),
        migrations.CreateModel(
            name='ElectionInfoRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=800)),
                ('contributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='electionInfoRequests', to='infoRequests.Contributor')),
                ('election', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='infoRequests', to='elections.Election')),
            ],
        ),
        migrations.AddField(
            model_name='candidateinforequest',
            name='contributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='candidateInfoRequests', to='infoRequests.Contributor'),
        ),
    ]
