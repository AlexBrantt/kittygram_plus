# Generated by Django 3.2 on 2024-06-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_auto_20240624_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
