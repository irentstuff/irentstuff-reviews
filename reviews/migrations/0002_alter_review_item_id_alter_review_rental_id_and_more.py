# Generated by Django 5.1.1 on 2024-09-14 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="item_id",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="review",
            name="rental_id",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="review",
            name="user_id",
            field=models.CharField(default="default_user", max_length=255),
        ),
    ]
