# Generated by Django 2.2.16 on 2020-09-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customtext',
            name='title',
        ),
        migrations.AddField(
            model_name='customtext',
            name='title234455',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
