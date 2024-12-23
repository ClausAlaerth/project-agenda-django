from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from contact.models import Contact
from django.core.exceptions import ValidationError

from django import forms

# Create your views here.


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
        )

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            "first_name",
            ValidationError(
                "mensagem de erro",
                code="invalid"
            )
        )

        self.add_error(
            "last_name",
            ValidationError(
                "mensagem de erro",
                code="invalid"
            )
        )

        return super().clean()


def create(request):
    if request.method == "POST":
        context = {
            "site_title": "Create Contact - ",
            "form": ContactForm(request.POST)
        }

        return render(
            request,
            "contact/create.html",
            context=context,
        )

    context = {
        "site_title": "Create Contact - ",
        "form": ContactForm()
    }

    return render(
        request,
        "contact/create.html",
        context=context,
    )
