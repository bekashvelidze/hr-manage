# Generated by Django 4.2 on 2023-12-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0004_paymenthistory_life_insurance_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="paymenthistory",
            name="time",
            field=models.TimeField(default="12:00:00"),
            preserve_default=False,
        ),
    ]
