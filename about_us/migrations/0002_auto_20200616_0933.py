# Generated by Django 3.0.7 on 2020-06-16 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutuspage',
            name='history_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='history_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='main_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='side_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
