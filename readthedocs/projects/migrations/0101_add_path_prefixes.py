# Generated by Django 3.2.18 on 2023-03-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0100_project_readthedocs_yaml_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalproject",
            name="custom_prefix",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="A custom path prefix used when serving documentation from this project. By default we serve documentation at the root (/) of a domain.",
                max_length=255,
                null=True,
                verbose_name="Custom path prefix",
            ),
        ),
        migrations.AddField(
            model_name="historicalproject",
            name="custom_subproject_prefix",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="A custom path prefix used when evaluating the root of a subproject. By default we serve documentation from subprojects under the `/projects/` prefix.",
                max_length=255,
                null=True,
                verbose_name="Custom subproject path prefix",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="custom_prefix",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="A custom path prefix used when serving documentation from this project. By default we serve documentation at the root (/) of a domain.",
                max_length=255,
                null=True,
                verbose_name="Custom path prefix",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="custom_subproject_prefix",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="A custom path prefix used when evaluating the root of a subproject. By default we serve documentation from subprojects under the `/projects/` prefix.",
                max_length=255,
                null=True,
                verbose_name="Custom subproject path prefix",
            ),
        ),
    ]