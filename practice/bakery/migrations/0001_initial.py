# Generated by Django 4.0.1 on 2022-03-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biscuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('flavour', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
