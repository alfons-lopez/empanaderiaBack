from django.db import models

# id, tipo, precio, img -- datos que se obtienen desde el json
class Empanada(models.Model):
    tipo =  models.CharField(max_length=200)
    precio = models.PositiveSmallIntegerField(blank=False,null=False)  
    img = models.ImageField(default='', upload_to='img/') 


    # darle un nombre en particular a la tabla -- da atributos extras a una clase
    class Meta:
        db_table = "empanada_tabla_django"

    def __str__(self):
        return f"Empanada de la región : {self.tipo}, Precio {self.precio}"
    
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]