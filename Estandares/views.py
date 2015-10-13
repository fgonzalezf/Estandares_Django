from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Documento,Versiones
class Home(TemplateView):
    template_name = "index.html"

class Tematicas(TemplateView):
    template_name = "tematicas.html"

class ListaDocumentos(ListView):
    template_name = "consulta.html"
    model = Documento
    def get(self, request, *args, **kwargs):
        busqueda = request.GET.get('tipo', '').upper()
        print busqueda
        Documentos= Documento.objects.filter(tipo__contains=busqueda)
        return render(request,'consulta.html',{'Documentos':Documentos})


# Create your views here.
