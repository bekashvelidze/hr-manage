# Generated by Django 4.2.6 on 2023-12-28 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_paymenthistory_loan_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymenthistory',
            name='loan_name',
        ),
    ]
