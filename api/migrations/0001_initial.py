# Generated by Django 5.1 on 2024-09-27 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('NON IT', 'NON IT'), ('Mobile', 'MOBILE')], max_length=100)),
                ('added_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
