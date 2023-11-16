from django.forms import ModelForm
from .models import Entrenador, Clase

class entrenadorForm(ModelForm):
    class Meta:
        model = Entrenador
        fields = '__all__'

class claseForm(ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'
