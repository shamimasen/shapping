from django.forms import ModelForm
from main.models import MoodEntry
from django.utils.html import strip_tags

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["product_name", "price", "description", "rating"]

    def clean_product(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)