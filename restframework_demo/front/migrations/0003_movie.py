# Generated by Django 2.0.1 on 2020-07-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=50)),
                ('m_price', models.FloatField(default=1)),
            ],
        ),
    ]