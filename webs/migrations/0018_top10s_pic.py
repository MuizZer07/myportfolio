# Generated by Django 2.1.5 on 2019-05-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0017_top10s'),
    ]

    operations = [
        migrations.AddField(
            model_name='top10s',
            name='pic',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]