# Generated by Django 3.2.17 on 2023-09-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_role_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('ME', 'ME'), ('CE', 'CE'), ('BSH', 'BSH'), ('None', 'None')], max_length=100)),
                ('seats', models.IntegerField()),
                ('admitted', models.IntegerField()),
            ],
        ),
    ]
