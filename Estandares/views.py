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
        if Documentos:
            datos=[]
            for documento in Documentos:
                versionesAnt= Versiones.objects.filter(codigo=documento.pk)
                datos.append(dict([(documento,versionesAnt)]))
            for dato in datos:
                print dato
                for documento,version in dato.items():
                    print documento.nombre
                    for doc in version:
                        print doc.url


        return render(request,'consulta.html',{'datos':datos})


# Create your views here.
