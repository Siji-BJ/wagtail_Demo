# Generated by Django 3.0.7 on 2020-06-13 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0018_auto_20200613_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='background_image_of_support',
            field=models.ForeignKey(blank=True, help_text='Background image of support Text ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
