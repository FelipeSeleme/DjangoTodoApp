# Generated by Django 5.1.4 on 2024-12-10 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='complete',
        ),
    ]