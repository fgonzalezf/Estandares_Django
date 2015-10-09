from django.db import models

class Documento (models.Model):
    nombre= models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    codigo= models.CharField(max_length=100)
    fechaPublicacion= models.DateField()
    vigencia= models.DateField()
    otrasVersiones = models.CharField(max_length=100)
    discucion = models.CharField(max_length=100)
    url= models.CharField(max_length=250)
    def __unicode__(self):
        return self.nombre


# Create your models here.
