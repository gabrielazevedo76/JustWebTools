from attr import fields
from django import forms

from watermark.models import WatermarkModel

class WatermarkForm(forms.ModelForm):
    class Meta:
        model = WatermarkModel
        fields = ['img', 'logo']

