# Generated by Django 4.1 on 2022-09-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nba", "0014_chart_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="chart",
            name="description",
            field=models.TextField(default=" ", max_length=500),
        ),
    ]
