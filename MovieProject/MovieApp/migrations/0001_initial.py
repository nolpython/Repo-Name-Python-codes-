# Generated by Django 2.1.5 on 2019-02-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyMovieModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateField()),
                ('movieName', models.CharField(max_length=50)),
                ('hero', models.CharField(max_length=50)),
                ('heroine', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
