# Generated by Django 4.1.1 on 2022-09-30 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
