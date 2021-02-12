from django import forms
from .models import Train

class TrainForm(forms.ModelsForm):
    class Meta:
        model = Train
        fields = ('name','registration_no',)


