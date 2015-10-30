from django.shortcuts import render
from django.http import HttpResponse
from merka2.models import Producto
from django.views.generic import CreateView, TemplateView, ListView
import datetime
from django.views import generic
from forms import ProductoForm
from django.core.context_processors import csrf


# Create your views here.
def raiz(request):
	"""Funcion que da la hora actual
	"""
	ahora = datetime.datetime.now()
	return render(request,'index.html')

def crear(request):
    if request.POST:
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = ProductoForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request,'crear_producto.html')
