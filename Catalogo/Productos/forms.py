from django.forms import ModelForm
from .models import Producto

#Este formulario trae todos los campos de la clase.
class productoForm(ModelForm):
    class Meta: #Esta SubClase aparece obligatoriamente para utilizar los formularios de Django. Se le indica el modelo y los campos de los cuales se va a #ocupar el formulario.
        model = Producto
        fields = '__all__'

#Este formulario traería solo los campos especificados.
#class frmProd2(ModelForm):
 #   class Meta:
  #      model = Producto
   #     fields = {
    #        'nombre',
     #       'precio'
      #  }