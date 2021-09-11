# Generated by Django 3.2.7 on 2021-09-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0008_alter_position_workers_num"),
    ]

    operations = [
        migrations.AddField(
            model_name="skill",
            name="level_rate",
            field=models.DecimalField(
                decimal_places=2, default=2, max_digits=5
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="skill",
            name="rate",
            field=models.DecimalField(
                decimal_places=2, default=2.22, max_digits=5
            ),
            preserve_default=False,
        ),
    ]
