from django.forms import ModelForm
from .models import Plan, Cuota, Alumno

class planForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

class cuotaForm(ModelForm):
    class Meta:
        model = Cuota
        fields = '__all__'

class alumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'