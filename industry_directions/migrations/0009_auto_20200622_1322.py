# Generated by Django 3.0.7 on 2020-06-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry_directions', '0008_auto_20200622_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='growthchart',
            name='svg',
        ),
        migrations.AddField(
            model_name='growthchart',
            name='link_url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
