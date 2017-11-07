from django import forms

from .models import *


class MesForm(forms.ModelForm):
    class Meta:
        model = Mes
        fields = ('nombre', 'monto',)


class ResidenteForm(forms.ModelForm):
    class Meta:
        model = Residente
        fields = ('nombre', 'apellido', 'email',)




class PagoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Pago
        fields = ('empleado','residente','fecha','meses','montototal')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.



def __init__ (self, *args, **kwargs):
    super(PagoForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.

    self.fields["meses"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget
    self.fields["meses"].help_text = "Ingrese los Meses a pagar"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

    self.fields["meses"].queryset = Mes.objects.all()
