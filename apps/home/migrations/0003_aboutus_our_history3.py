# Generated by Django 5.2 on 2025-04-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_aboutus_our_history_aboutus_our_history1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='our_history3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
