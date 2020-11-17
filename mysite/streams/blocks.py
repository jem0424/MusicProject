"""Streamfields live in here"""


from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text= 'Add your title')
    text = blocks.TextBlock(required=True, help_text= 'Add additional text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class CardBlock(blocks.StructBlock):
    """"Cards with image and text"""

    title = blocks.CharBlock(required=True, help_text="Add Text Here")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text",blocks.TextBlock(required=True, max_length=200)),
                ("button_page",blocks.PageChooserBlock(required=True)),
                ("button_url",blocks.URLBlock(required=False, help_text="If button is selected above, that will be used first")),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"

class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"

class CTABlock(blocks.StructBlock):
    """call to action section"""
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features =["bold","italic"])
    button_page = blocks.PageChooserBlock(required=False) #internal
    button_url = blocks.URLBlock(required=False) #external
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length= 40)


    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"