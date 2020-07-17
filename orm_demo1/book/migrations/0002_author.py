# Generated by Django 2.0.2 on 2020-07-15 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
                ('age', models.IntegerField(db_column='kangbazi_age', default=18, null=True)),
                ('telephone', models.CharField(max_length=11, unique=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
