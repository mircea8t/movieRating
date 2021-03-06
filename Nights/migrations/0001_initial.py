# Generated by Django 3.1.4 on 2021-01-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='movie_pics')),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=200)),
            ],
        ),
    ]
