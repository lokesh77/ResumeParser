# Generated by Django 2.1.7 on 2019-04-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0003_remove_resume_year_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='educations',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Educations'),
        ),
    ]
