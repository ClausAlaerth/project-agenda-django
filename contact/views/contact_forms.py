from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from contact.models import Contact

# Create your views here.


def create(request):
    if request.method == "POST":
        print()
        print(request.method)
        print(request.POST.get("first_name"))
        print(request.POST.get("last_name"))
        print()

    context = {

    }

    print()
    print(request.method)
    print()

    return render(
        request,
        "contact/create.html",
        context=context,
    )
