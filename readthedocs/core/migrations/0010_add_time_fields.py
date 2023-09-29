# Generated by Django 2.2.24 on 2021-11-11 19:08

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0009_historicaluserprofile"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userprofile",
            options={"get_latest_by": "modified"},
        ),
        migrations.AddField(
            model_name="historicaluserprofile",
            name="created",
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True, null=True, verbose_name="created"
            ),
        ),
        migrations.AddField(
            model_name="historicaluserprofile",
            name="modified",
            field=django_extensions.db.fields.ModificationDateTimeField(
                auto_now=True, null=True, verbose_name="modified"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="created",
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True, null=True, verbose_name="created"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="modified",
            field=django_extensions.db.fields.ModificationDateTimeField(
                auto_now=True, null=True, verbose_name="modified"
            ),
        ),
    ]
