# Generated by Django 2.2.3 on 2019-07-14 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_auto_20190714_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='classinfo',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
