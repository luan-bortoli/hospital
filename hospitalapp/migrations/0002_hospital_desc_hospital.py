# Generated by Django 3.1.3 on 2020-11-30 03:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='desc_hospital',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
