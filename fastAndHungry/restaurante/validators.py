from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible

from users.models import *

#Create your validators here.

@deconstructible
class IsDeliveryManValidator(object):

    def __call__ (self, value):
        user = User.objects.get(id=value)
        if not user.is_delivery_man:
            raise ValidationError(
                _('%(value)s no es un repartidor'),
                params={'value': user},
            )


@deconstructible
class IsAdminValidator(object):

    def __call__ (self, value):
        user = User.objects.get(id=value)
        if not user.is_admin:
            raise ValidationError(
                _('%(value)s no es un administrador'),
                params={'value': user},
            )


@deconstructible
class IsUserAddress(object):

    def __init__ (self, user, role):
        self.user = user
        self.role = role

    def __call__ (self, value):
        address = Address.objects.get(id=value)
        user = address.usuario
        if not user == self.user:
            raise ValidationError(
                _('La dirección no pertenece al %(role)s. Usuario esperado: %(user)s, Usuario recibido: %(ad_user)s'),
                params={ 'role': self.role , 'user' : self.user , 'ad_user' : user},
            )