# Generated by Django 2.0.6 on 2018-06-14 14:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_project_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='hearted_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='hearted_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
