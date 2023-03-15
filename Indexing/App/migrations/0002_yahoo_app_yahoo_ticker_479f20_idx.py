# Generated by Django 3.2.15 on 2022-08-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='yahoo',
            index=models.Index(fields=['ticker', 'date'], name='App_yahoo_ticker_479f20_idx'),
        ),
    ]
