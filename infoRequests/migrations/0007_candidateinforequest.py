# Generated by Django 2.1.5 on 2019-01-26 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_candidate_state'),
        ('infoRequests', '0006_auto_20190126_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateInfoRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=800)),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.Candidate')),
                ('contributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='infoRequests.Contributor')),
            ],
        ),
    ]
