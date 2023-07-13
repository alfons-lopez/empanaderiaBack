from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Empanada

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


# clase base
class EmpanadaBaseView():
    # atributos de clase
    template_name = "empanadas.html"        ## son todas las empanadas que tengo desplegados
    model = Empanada                        ## el modelo que trabaja
    fields = "__all__"                      ## campos que se van a mostrar -- puede ser por medio de tuplas
    success_url = reverse_lazy("empanadas:all")   ## la creacion o la vista se haya creado con exito, nos lleva a un lugar(reverse_lazy) (alias)


# CRUD

# lista con todos las empanadas que se crearon
class EmpanadaListView(EmpanadaBaseView, ListView):  ## por herencial se lo traspasa
    """
    Muestra todas las Empanadas
    """ 

    # detalles -- cuando quiero un Empanada
class EmpanadaDetailView(EmpanadaBaseView, DetailView):  # que se muestre solo uno
    template_name = "empanadas_detail.html"
    # cuando hace un success_url va al mismo lugar

class EmpanadaCreateView(EmpanadaBaseView, CreateView):
    template_name = "empanadas_create.html"
    extra_context = {
        "tipo" : "Crear empanada"
    }

class EmpanadaUpdateView(EmpanadaBaseView, UpdateView):
    template_name = "empanadas_create.html"
    extra_context = {
        "tipo" : "Actualizar empanada"
    }

class EmpanadaDeleteView(EmpanadaBaseView, DeleteView):
    template_name = "empanadas_delete.html"
    extra_context = {
        "tipo" : "Borrar empanada"
    }

