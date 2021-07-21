# Generated by Django 3.2.4 on 2021-07-21 06:47

from django.db import migrations

import weblate.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0016_alter_auditlog_activity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="verifiedemail",
            name="email",
            field=weblate.utils.fields.EmailField(max_length=190),
        ),
    ]
