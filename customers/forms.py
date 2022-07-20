from django.forms import ModelForm
from .models import *


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'