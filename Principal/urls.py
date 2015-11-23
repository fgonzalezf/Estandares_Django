"""Principal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Estandares.views import Home,Tematicas,ListaDocumentos,FormularioConsultaView,Busqueda

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Estandares/$', Home.as_view(), name= "Home"),
    url(r'^Estandares/tematicas',Tematicas.as_view(), name="Tematicas"),
    url(r'^Estandares/consulta',ListaDocumentos.as_view(),name="Consulta"),
    url(r'^Estandares/formulario',FormularioConsultaView.as_view(),name= "Formulario_Consulta_publica"),
    url(r'^Estandares/Guardado',FormularioConsultaView.as_view(),name="Guardado"),
    url(r'^Estandares/busqueda',Busqueda.as_view(),name="Busqueda"),



]
