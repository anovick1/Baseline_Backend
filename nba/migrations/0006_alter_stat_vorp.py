# Generated by Django 4.1 on 2022-09-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nba", "0005_alter_player_player_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stat",
            name="vorp",
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]
