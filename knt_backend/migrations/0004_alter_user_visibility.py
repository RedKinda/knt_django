# Generated by Django 4.2.1 on 2023-05-12 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("knt_backend", "0003_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="visibility",
            field=models.BooleanField(default=True),
        ),
    ]
