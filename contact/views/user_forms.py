from django.shortcuts import render
from contact.forms import RegisterForm


def register(request):

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        "title": "Registrar Usuário - ",
        "form": form
    }

    return render(
        request,
        "contact/register.html",
        context=context
    )
