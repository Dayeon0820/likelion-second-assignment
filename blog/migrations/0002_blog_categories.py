# Generated by Django 5.0.3 on 2024-03-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.CharField(default='default', max_length=50),
        ),
    ]
