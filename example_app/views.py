from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import MyModelForm, MyModelFormset


def add_mymodel(request):
    form = MyModelForm()
    context = {"form": form}
    return render(request, "form.html", context)
