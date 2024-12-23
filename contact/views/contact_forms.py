from django.shortcuts import render

from contact.forms import ContactForm


# Create your views here.


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
