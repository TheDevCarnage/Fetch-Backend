# Generated by Django 4.2.6 on 2023-10-09 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=255, unique=True)),
                ("total_points", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Payer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payer_name", models.CharField(max_length=255)),
                ("points_given", models.IntegerField()),
                ("paid_at", models.DateTimeField(auto_now_add=True)),
                (
                    "paid_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rewards.users"
                    ),
                ),
            ],
        ),
    ]
