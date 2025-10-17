from django import forms
from unfold.admin import ModelAdmin  # Assuming you're using Unfold
from .models import Seo

class SeoAdminForm(forms.ModelForm):
    meta_keywords = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. seo, marketing, universities",
            "class": "w-full"
        }),
        help_text="Enter keywords separated by commas."
    )

    class Meta:
        model = Seo
        fields = '__all__'

    def clean_meta_keywords(self):
        # Clean and normalize keywords
        raw = self.cleaned_data.get("meta_keywords", "")
        return ", ".join([kw.strip() for kw in raw.split(",") if kw.strip()])
