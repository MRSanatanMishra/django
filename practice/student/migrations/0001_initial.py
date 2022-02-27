# Generated by Django 4.0.1 on 2022-02-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentIfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('standard', models.IntegerField()),
                ('dob', models.DateField()),
                ('totalMarks', models.FloatField()),
            ],
        ),
    ]