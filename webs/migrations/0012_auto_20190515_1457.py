# Generated by Django 2.1.5 on 2019-05-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0011_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='feature',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='platform',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True),
        ),
    ]
