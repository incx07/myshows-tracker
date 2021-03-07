from .models import SerialComplete
from django.forms import ModelForm, TextInput, Select


RATING_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
]


class RatingForm(ModelForm):
    class Meta:
        model = SerialComplete
        fields = ['rating']
        widgets = {'rating': Select(choices=RATING_CHOICES,
                                    attrs={'class':'custom-select custom-select-sm'})}
