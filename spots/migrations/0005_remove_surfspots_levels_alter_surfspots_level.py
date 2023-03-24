# Generated by Django 4.1.7 on 2023-03-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0004_surfspots_levels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surfspots',
            name='levels',
        ),
        migrations.AlterField(
            model_name='surfspots',
            name='level',
            field=models.CharField(choices=[('BtP', 'Beginner Pro'), ('ItP', 'Intermediate Pro'), ('AtP', 'Advanced Pro'), ('P', 'Pro')], default=None, max_length=100),
        ),
    ]
