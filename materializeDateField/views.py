from django.shortcuts import render

from django.views import generic

from .models import ExampleModel

class ExampleModelUpdate(generic.edit.UpdateView):
    model = ExampleModel
    fields= ['endDate']
    template_name_suffix = '_update_form'

class ExampleModelCreate(generic.edit.CreateView):
    model = ExampleModel
    fields = ['endDate']
