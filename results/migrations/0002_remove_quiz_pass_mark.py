# Generated by Django 5.0.2 on 2024-03-07 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='pass_mark',
        ),
    ]
