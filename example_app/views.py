from django.forms import formset_factory
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import MyModelForm, CustomFormRenderer, OtherFormRenderer


def add_mymodel(request):
    form = MyModelForm()
    context = {"form": form}
    return render(request, "form.html", context)


def add_mymodels(request):
    # The issue is that here, we'd expect the MyModelForm.default_renderer to
    # be used here. Instead, the renderer defined in settings.FORM_RENDERER
    # is used.
    MyModelFormset = formset_factory(MyModelForm, extra=2)

    formset = MyModelFormset()
    context = {"formset": formset}
    return render(request, "formset.html", context)
