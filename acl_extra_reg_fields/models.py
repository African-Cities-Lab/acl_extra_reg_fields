from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    class Meta:
        app_label = "acl_extra_reg_fields"

    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE, null=True)
    SOCIAL_NETWORKS = (
        ('ln', 'Linkedin'),
        ('fb', 'Facebook'),
        ('yt', 'Youtube'),
        ('in', 'Instagram'),
        ('tk', 'TikTok'),
        ('pn', 'personal Network'),
        ('pfn', 'Professional Network'),
        ('ot', 'Other Network'),
    )
    LANGUAGES = (
        ('en', 'English'),
        ('fr', 'French')
    )

    preferred_language = models.CharField(
        verbose_name="Preferred Language",
        choices=LANGUAGES,
        max_length=100,
        blank=False 
    )
    referrer = models.CharField(
        verbose_name="How did you hear about the platfrom?",
        choices=SOCIAL_NETWORKS,
        max_length=50,
        blank=False 
    )

