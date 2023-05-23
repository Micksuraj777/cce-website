# Generated by Django 3.2.17 on 2023-05-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_hero_image_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero_image',
            name='page',
            field=models.CharField(choices=[('management', 'Management'), ('directors_desk', 'Directors Desk'), ('facilities', 'Facilities'), ('principals_desk', "Principal's Desk"), ('cce_in_media', 'CCE In Media'), ('governing_body', 'Governing Body'), ('organogram', 'Organogram'), ('mandatory_disclosure', 'Mandatory Disclosure'), ('antiraging_cell', 'AntiRaging Cell'), ('grivence_redressal_sysytem', 'Grivence Redressal System'), ('sc_st_monitoring_commite', 'Sc/St Monitoring Commitee'), ('iqac', 'IQAC'), ('examination_cell', 'Examination Cell'), ('pta', 'PTA'), ('office', 'office'), ('nss', 'NSS'), ('college_union', 'College Union'), ('facilities', 'Facilities'), ('pta', 'PTA'), ('None', 'None'), ('research', 'Research'), ('arts', 'Arts'), ('sports', 'Sports'), ('placements', 'Placements'), ('admissions', 'Admissions'), ('academic_research', 'Academic Research'), ('womencell', 'Women Cell'), ('clubs', 'Clubs'), ('iic', 'IIC'), ('all_committees', 'All Committees'), ('programs_offered', 'Progrmas Offered'), ('hr_manual', 'HR Manual'), ('vision_2035', 'Vision 2035'), ('annual_report', 'Annual Report'), ('college_handbook', 'College Handbook'), ('college_calendar', 'College Calendar'), ('audited_statements', 'Audited Statements'), ('college_magazine', 'College Magazine'), ('ktu_aicte_regulations', 'KTU AICTE Regulations'), ('approvals', 'Approvals'), ('techies_park', 'Techies Park'), ('events', 'Events')], default='None', max_length=200),
        ),
    ]
