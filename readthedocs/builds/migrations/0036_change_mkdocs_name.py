# Generated by Django 2.2.23 on 2021-06-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builds", "0035_backport_indexes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="documentation_type",
            field=models.CharField(
                choices=[
                    ("sphinx", "Sphinx Html"),
                    ("mkdocs", "Mkdocs"),
                    ("sphinx_htmldir", "Sphinx HtmlDir"),
                    ("sphinx_singlehtml", "Sphinx Single Page HTML"),
                    ("mkdocs_html", "Mkdocs Html Pages"),
                ],
                default="sphinx",
                help_text="Type of documentation the version was built with.",
                max_length=20,
                verbose_name="Documentation type",
            ),
        ),
    ]