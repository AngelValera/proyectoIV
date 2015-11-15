from django.shortcuts import render
from django.http import HttpResponse
from merka.models import Seccion, Producto


def index(request):
    context_dict = {}

    secciones = Seccion.objects.all()
    context_dict['secciones']= secciones

    productos = Producto.objects.all()[:5]
    context_dict['productos']= productos
    # Render the response and send it back!
    return render(request, 'merka/index.html', context_dict)


def seccion(request, seccion_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:

        seccion = Seccion.objects.get(slug=seccion_name_slug)
        context_dict['seccion_name'] = seccion.nombre

        productos = Producto.objects.filter(seccion=seccion)

        # Adds our results list to the template context under name pages.
        context_dict['productos'] = productos
        context_dict['seccion'] = seccion
    except Seccion.DoesNotExist:
        pass

    # Go render the response and return it to the client.
    return render(request, 'merka/seccion.html', context_dict)
