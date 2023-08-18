from django import forms
from .models import Event, Registration

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date', 'location', 'is_published')

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('event',)
