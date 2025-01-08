from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


# Create your views here.


def create(request):

    form_action = reverse("contact:create")

    if request.method == "POST":

        form = ContactForm(request.POST, request.FILES)

        context = {
            "site_title": "Create Contact - ",
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():

            contact = form.save()

            return redirect("contact:update", contact_id=contact.pk)

        return render(
            request,
            "contact/create.html",
            context=context,
        )

    context = {
        "site_title": "Create Contact - ",
        "form": ContactForm(),
        "form_action": form_action,
    }

    return render(
        request,
        "contact/create.html",
        context=context,
    )


def update(request, contact_id):

    contact = get_object_or_404(Contact, id=contact_id, show=True)

    form_action = reverse("contact:update", args=(contact_id,))

    if request.method == "POST":

        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            "site_title": "Update Contact - ",
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():

            contact = form.save()

            return redirect("contact:update", contact_id=contact.pk)

        return render(
            request,
            "contact/create.html",
            context=context,
        )

    context = {
        "site_title": "Update Contact - ",
        "form": ContactForm(instance=contact),
        "form_action": form_action,
    }

    return render(
        request,
        "contact/create.html",
        context=context,
    )


def delete(request, contact_id):

    contact = get_object_or_404(Contact, id=contact_id, show=True)

    confirmation = request.POST.get("confirmation", "no")

    if confirmation == "yes":
        contact.delete()
        return redirect("contact:index")

    context = {
        "site_title": "Delete Contact - ",
        "contact": contact,
        "confirmation": confirmation,
    }

    return render(
        request,
        "contact/contact.html",
        context=context
    )
