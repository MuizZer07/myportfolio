# Generated by Django 2.1.5 on 2019-05-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0018_top10s_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='top10s',
            old_name='pic',
            new_name='pic1',
        ),
        migrations.AddField(
            model_name='top10s',
            name='pic2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='top10s',
            name='pic3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='top10s',
            name='pic4',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
