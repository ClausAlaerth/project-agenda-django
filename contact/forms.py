from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

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


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True,
        min_length=3,
    )

    class Meta:

        model = User

        fields = (
            "first_name", "last_name", "email",
            "username", "password1", "password2",
        )

    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():

            self.add_error(
                "email",
                ValidationError("Esse e-mail já existe.", code="invalid")
            )

        return email
