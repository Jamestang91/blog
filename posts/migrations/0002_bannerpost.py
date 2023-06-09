# Generated by Django 4.1.7 on 2023-03-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bannerpost",
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
                ("bannerUrl", models.CharField(max_length=500)),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=1000)),
                ("breakPage", models.CharField(max_length=500)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
