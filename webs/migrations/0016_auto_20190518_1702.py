# Generated by Django 2.1.5 on 2019-05-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0015_filebin_textbin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filebin',
            name='imp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='textbin',
            name='imp',
            field=models.BooleanField(default=False),
        ),
    ]