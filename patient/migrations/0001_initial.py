# Generated by Django 3.2.8 on 2021-10-28 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='patient', serialize=False, to='user.user')),
                ('job', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
