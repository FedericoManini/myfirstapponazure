from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                    "placeholder": "Nome"
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                    "placeholder": "Descrizione"
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "forms-control",
                    'placeholder': 'Numero di clienti controllati'
                }
            )
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "")
        description = cleaned_data.get("description", "")
        price = cleaned_data.get("price")

        if not name:
            self.add_error("name", "Il campo nome è richiesto")
        if not description:
            self.add_error("description", "impegnati di più")
        if price is None or price == 0:
            self.add_error("price", "Il campo Prezzo è richiesto")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = True
        self.fields["name"].required = True
        self.fields['price'].initial = 0
