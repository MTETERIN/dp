# Generated by Django 2.2.5 on 2019-09-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('data', models.CharField(max_length=150)),
                ('created_at', models.DateField()),
            ],
        ),
    ]
