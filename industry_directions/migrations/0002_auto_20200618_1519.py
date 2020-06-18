# Generated by Django 3.0.7 on 2020-06-18 09:49

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('industry_directions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='industrydirectionspage',
            name='body_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='industrydirectionspage',
            name='body_text_1',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='industrydirectionspage',
            name='body_text_2',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='industrydirectionspage',
            name='body_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
