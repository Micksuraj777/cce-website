# Generated by Django 3.2.13 on 2023-02-16 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0016_grivencecommitee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicadministractors',
            name='faculty',
        ),
        migrations.DeleteModel(
            name='AcademicAdministrationDirector',
        ),
        migrations.RemoveField(
            model_name='examinationcellfaculty',
            name='faculty',
        ),
        migrations.DeleteModel(
            name='GrivenceCommitee',
        ),
        migrations.DeleteModel(
            name='MandatoryDisclosure',
        ),
        migrations.DeleteModel(
            name='AcademicAdministractors',
        ),
        migrations.DeleteModel(
            name='ExaminationCellFaculty',
        ),
    ]
