from django.forms import formset_factory
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import MyModelForm, CustomFormRenderer, OtherFormRenderer


def add_mymodel(request):
    form = MyModelForm()
    context = {"form": form}
    return render(request, "form.html", context)


def add_mymodels(request):
    MyModelFormset = formset_factory(MyModelForm, renderer=OtherFormRenderer())
    formset = MyModelFormset()
    context = {"formset": formset}
    return render(request, "formset.html", context)
