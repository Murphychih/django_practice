# Generated by Django 3.0.5 on 2022-10-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_app_project_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='app',
            field=models.ManyToManyField(to='myapp.App'),
        ),
    ]
