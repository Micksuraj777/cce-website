# Generated by Django 4.0.4 on 2022-09-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_homeupdates'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('sub_heading', models.CharField(max_length=50)),
                ('sub_text', models.CharField(max_length=100)),
            ],
        ),
    ]
