# Generated by Django 3.0.4 on 2020-04-03 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0066_merge_20200401_0038"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectslug",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="slugs",
                to="api.Project",
            ),
        ),
        migrations.AlterField(
            model_name="repositoryslug",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="slugs",
                to="api.Repository",
            ),
        ),
        migrations.AlterField(
            model_name="taskslug",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="slugs",
                to="api.Task",
            ),
        ),
    ]