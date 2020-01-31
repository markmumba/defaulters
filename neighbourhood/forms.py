from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']


class DateInput(forms.DateInput):
    input_type = 'date'

class DefaulterForm(forms.ModelForm):
    class Meta:
        model=defaulter
        exclude=['username','neighbourhood']
        widgets = {
            'from_date': DateInput(),
            'to_date': DateInput(),

        }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
    
class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']
    
class notificationsForm(forms.ModelForm):
    class Meta:
        model=notifications
        exclude=['author','neighbourhood','post_date']