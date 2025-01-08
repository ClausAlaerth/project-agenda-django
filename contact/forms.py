from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):

    pictures = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*"
            }
        )
    )

    class Meta:
        model = Contact

        fields = (
            "first_name", "last_name", "phone",
            "email", "description", "category",
            "pictures",
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:

            msg = ValidationError(
                "Primeiro e segundo nome não podem ser iguais.",
                code="invalid"
            )

            self.add_error("first_name", msg)
            self.add_error("last_name", msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if first_name == "ABC":
            self.add_error(
                "first_name",
                ValidationError(
                    "veio do add_error first_name",
                    code="invalid"
                )
            )

        return first_name
