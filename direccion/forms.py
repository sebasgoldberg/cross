from django.forms.widgets import Select
from django.forms import ModelForm, ModelChoiceField
from django.forms.util import ErrorList
from cities_light.models import Country, Region
from iampacks.cross.direccion.models import Ciudad
from iampacks.cross.direccion.models import COUNTRY_FILTER
from django.utils.translation import ugettext as _

class BaseDireccionForm(ModelForm):
  pass
 
