# Generated by Django 5.0.2 on 2024-04-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0006_alter_skill_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('company_name', models.CharField(blank=True, default='', max_length=254, verbose_name='Company Name')),
                ('job_title', models.CharField(blank=True, default='', max_length=254, verbose_name='Job Title')),
                ('job_location', models.CharField(blank=True, default='', max_length=254, verbose_name='Job Location')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
                'ordering': ('start_date',),
            },
        ),
    ]
