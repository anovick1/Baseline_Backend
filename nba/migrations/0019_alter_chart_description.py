# Generated by Django 4.1 on 2022-09-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nba", "0018_alter_chart_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chart",
            name="description",
            field=models.CharField(default=" ", max_length=255),
        ),
    ]
