from django.db import models

# vamos a crear las propiedades de los atributos.
class Usuario(models.Model):
    genero_eleccion = (
        ('M','Masculino'),
        ('F', 'Femenino'), 
    )
    
    codigo = models.IntegerField()
    # ponemos que queremos la foto con el año, mes y día
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    #para el genero elegirá el que corresponda
    genero = models.CharField(choices=genero_eleccion, max_length=100)
    ciudad = models.CharField(max_length=100)
    
    # por el tema de las fotos saldrá un error de pillow hay que instalarlo pip install pillow
    
    # si yo quisiera que se mostrarán al detalle todos los usuarios
    
    def __str__(self):
        return self.nombre