from django.forms import ModelForm
from .models import Telefono

class TelefonoForm(ModelForm):
    class Meta:
        model = Telefono
        fields = "__all__"
