# Generated by Django 4.1 on 2022-09-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nba", "0012_alter_like_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="pfp_url",
            field=models.TextField(
                default="https://st4.depositphotos.com/1000507/24489/v/600/depositphotos_244890858-stock-illustration-user-profile-picture-isolate-background.jpg"
            ),
        ),
    ]