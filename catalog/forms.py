import os

from django import forms
from dotenv import load_dotenv

from catalog.models import Product

load_dotenv()

FORBIDDEN_WORDS = os.getenv("FORBIDDEN_WORDS").split(", ")


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs.update({"class": "form-check-input"})
            else:
                field.widget.attrs.update({"class": "form-control"})


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock", "image", "category"]

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("Цена продукта не может быть отрицательной.")
        return price

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(word in name.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError("Имя продукта содержит запрещенные слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if any(word in description.lower() for word in FORBIDDEN_WORDS):
            raise forms.ValidationError("Описание продукта содержит запрещенные слова.")
        return description
