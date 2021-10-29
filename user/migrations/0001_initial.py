# Generated by Django 3.2.8 on 2021-10-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='이름')),
                ('age', models.IntegerField(null=True, verbose_name='나이')),
                ('phone_number', models.CharField(max_length=20, null=True, verbose_name='전화번호')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2, null=True, verbose_name='성별')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='주소')),
                ('joined_date', models.DateTimeField(auto_now_add=True, verbose_name='가입년월일')),
                ('user_type', models.CharField(choices=[('P', 'Patient'), ('D', 'Doctor')], max_length=2, verbose_name='유저타입')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
