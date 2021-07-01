from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    header = RichTextField(blank=True)

    # define multiple image types
    amphibian = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    animal = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    arachnid = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    bird = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    chromist = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    fish = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    fungi = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    insect = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    mammal = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    mollusc = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    plant = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    protozoa = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )
    reptile = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('header', classname="full"),
        ImageChooserPanel('amphibian'),
        ImageChooserPanel('animal'),
        ImageChooserPanel('arachnid'),
        ImageChooserPanel('bird'),
        ImageChooserPanel('chromist'),
        ImageChooserPanel('fish'),
        ImageChooserPanel('fungi'),
        ImageChooserPanel('insect'),
        ImageChooserPanel('mammal'),
        ImageChooserPanel('mollusc'),
        ImageChooserPanel('plant'),
        ImageChooserPanel('protozoa'),
        ImageChooserPanel('reptile'),
    ]
