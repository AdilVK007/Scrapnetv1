# Generated by Django 5.0.3 on 2024-03-28 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='USER',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='aadhar_no',
            field=models.CharField(default='', max_length=100),
        ),
    ]
