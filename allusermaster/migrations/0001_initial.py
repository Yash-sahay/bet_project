# Generated by Django 4.2.3 on 2023-07-07 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(blank=True, max_length=20, null=True)),
                ('agent_limit', models.CharField(max_length=20)),
                ('agent_share', models.CharField(max_length=20)),
                ('match_commission', models.CharField(max_length=20)),
                ('session_commission', models.CharField(max_length=20)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuperAgentMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(blank=True, max_length=10, null=True)),
                ('super_agent_limit', models.CharField(max_length=20)),
                ('super_agent_share', models.CharField(max_length=20)),
                ('match_commission', models.CharField(max_length=20)),
                ('session_commission', models.CharField(max_length=20)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(blank=True, max_length=10, null=True)),
                ('client_limit', models.CharField(max_length=20)),
                ('match_commission', models.CharField(max_length=20)),
                ('session_commission', models.CharField(max_length=20)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('agent_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allusermaster.agentmaster')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='agentmaster',
            name='super_agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allusermaster.superagentmaster'),
        ),
        migrations.AddField(
            model_name='agentmaster',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
