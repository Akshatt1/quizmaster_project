# Generated by Django 4.2.11 on 2025-01-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=25)),
                ('data', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
