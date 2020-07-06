# Generated by Django 3.0.7 on 2020-07-06 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('contactus', '0003_auto_20200616_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactuspage',
            name='header_image',
            field=models.ForeignKey(help_text='Landscape mode only; Approximate dimensions: 1440 px (width) x 360 px (height)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
