# Generated by Django 5.0 on 2024-01-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biteblaze', '0002_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('quentity', models.IntegerField()),
                ('address', models.CharField(max_length=400)),
                ('contact', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=50)),
                ('username', models.CharField(max_length=40)),
            ],
        ),
    ]
