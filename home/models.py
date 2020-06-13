from django.db import models
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page,Orderable
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)

class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Homepage image'
    )
    vision_title = models.CharField(
        null=True,
        blank=False,
        default='Vision',
        max_length=100,
        help_text='Vision'
    )
    vision_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Vision image'
    )
    vision_text = RichTextField(
        null=True,
        blank=False,
        default=' ',
        max_length=400,
        help_text='Write vision'
    )
    mission_title = models.CharField(
        blank=False,
        default='Mission',
        max_length=250,
        help_text='Mission title'
    )
    objectives_title = models.CharField(
        blank=False,
        default='Objectives',
        max_length=250,
        help_text='Objective title'
        )
    objectives_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Background Image Of Objectives Section'
    )
    objectives_side_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image displayed in the right side of objectives section'
    )
    usp_title = models.CharField(
        blank=False,
        default='Our USP',
        max_length=250,
        help_text='USP section title'
    )
    usp_side_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image to be displayed inside USP secton'
    )
    contact_us_button_text = models.CharField(
        blank=True,
        default='Contact with Us',
        max_length=250,
        help_text='Text displayed inside the contact us button'
        )
    image_inside_contact_us_button = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Arrow displayed inside the contact us button '
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel(
            'image',heading="Home Page"),
        MultiFieldPanel([
            FieldPanel('vision_title', classname="full"),
            ImageChooserPanel('vision_image'),
            FieldPanel('vision_text', classname="full"),
        ], heading="Vision section"),
        MultiFieldPanel([
            FieldPanel('mission_title',classname="full"),
            InlinePanel('missions',label="Mission"),
        ], heading="Missions"),
        MultiFieldPanel([
            FieldPanel('objectives_title',classname="full"),
            ImageChooserPanel('objectives_background_image',classname="full"),
            ImageChooserPanel('objectives_side_image',classname="full"),
            InlinePanel('objectives',label="Objective"),
        ], heading="Objectives"),
        MultiFieldPanel([
            FieldPanel('usp_title',classname='full'),
            ImageChooserPanel('usp_side_image',classname='full'),
            FieldPanel('contact_us_button_text',classname='full'),
            ImageChooserPanel('image_inside_contact_us_button',classname='full'),
            InlinePanel('usps',label="USP")
        ])
        
    ]


class Mission(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='missions')
    list_label = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='List label'
    )
    mission = models.CharField(
        blank=False,
        default=' ',
        max_length=250
    )
    panels= [
        ImageChooserPanel('list_label'),
        FieldPanel('mission')
    ]


class Objective(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='objectives')
    objective_text = models.CharField(
        blank=False,
        default=' ',
        max_length=250
    )
    objective_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Images of Objectives'
    )
    panels = [
        FieldPanel('objective_text'),
        ImageChooserPanel('objective_image')
    ]

class USP(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='usps')
    usp= models.CharField(
        blank=False,
        default=' ',
        max_length=250
    )
    panels = [
        FieldPanel('usp')
    ]