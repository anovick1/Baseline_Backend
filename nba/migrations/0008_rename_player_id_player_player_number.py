# Generated by Django 4.1 on 2022-09-02 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nba", "0007_alter_stat_vorp"),
    ]

    operations = [
        migrations.RenameField(
            model_name="player", old_name="player_id", new_name="player_number",
        ),
    ]
