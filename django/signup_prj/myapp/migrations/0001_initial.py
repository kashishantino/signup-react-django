# Generated by Django 4.2.1 on 2023-06-27 05:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('phone', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('is_eligible', models.BooleanField(blank=True, null=True)),
                ('is_valid', models.BooleanField(blank=True, default=True, null=True)),
                ('is_staff', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'db_table': 'myapp',
            },
        ),
    ]
