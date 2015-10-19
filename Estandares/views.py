from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Documento,Versiones,FormularioConsulta
from django.core.urlresolvers import reverse_lazy
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
        datos=[]
        if Documentos:
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

class FormularioConsultaView(CreateView):
    template_name = 'Formulario.html'
    model = FormularioConsulta
    fields = '__all__'
    success_url = reverse_lazy('Guardado')

# Create your views here.
