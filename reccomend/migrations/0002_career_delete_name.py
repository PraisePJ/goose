# Generated by Django 4.1.4 on 2022-12-12 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reccomend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]
