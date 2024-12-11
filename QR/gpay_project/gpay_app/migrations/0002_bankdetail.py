# Generated by Django 3.2 on 2024-11-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpay_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=20)),
                ('ifsc_code', models.CharField(max_length=20)),
            ],
        ),
    ]
