# Generated by Django 4.2.5 on 2023-11-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(help_text='Format: YYYY-MM-DD', verbose_name='Payment Date'),
        ),
    ]