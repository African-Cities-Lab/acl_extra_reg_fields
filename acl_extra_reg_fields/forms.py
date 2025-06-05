from django import forms
from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # This ensures the frontend gets only string-based error messages
        self.fields['referrer'].error_messages = "This field is required."
        self.fields['preferred_language'].error_messages = "This field is required."

    referrer = forms.ChoiceField(
        choices=ExtraInfo.SOCIAL_NETWORKS,
        required=True,
        label="How did you hear about the platform?",
        widget=forms.Select(),
        
    )

    preferred_language = forms.ChoiceField(
        choices=ExtraInfo.LANGUAGES,
        required=True,
        label="Preferred Language",
        widget=forms.Select(),
        
    )

    class Meta:
        model = ExtraInfo
        fields = ('referrer', 'preferred_language')
