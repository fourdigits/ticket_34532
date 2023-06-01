from django import forms
from django.forms.renderers import TemplatesSetting

from .models import MyModel


class CustomFormRenderer(TemplatesSetting):
    form_template_name = "form_snippet.html"


class OtherFormRenderer(TemplatesSetting):
    form_template_name = "form_snippet_other.html"


class MyModelForm(forms.ModelForm):
    # Commenting out the next line makes the form use the FORM_RENDERER from settings.py
    default_renderer = CustomFormRenderer

    class Meta:
        model = MyModel
        exclude = []
