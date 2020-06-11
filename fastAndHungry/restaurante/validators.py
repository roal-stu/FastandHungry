from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible

from users.models import *

#Create your validators here.

@deconstructible
class IsDeliveryManValidator(object):

    def __call__ (self, value):
        if not value.is_delivery_man:
            raise ValidationError(
                _('%(value)s no es un repartidor'),
                params={'value': value},
            )


@deconstructible
class IsAdminValidator(object):

    def __call__ (self, value):
        if not value.is_admin:
            raise ValidationError(
                _('%(value)s no es un administrador'),
                params={'value': value},
            )


@deconstructible
class IsUserAddress(object):

    def __init__ (self, user, role):
        self.user = user
        self.role = role

    def __call__ (self, value):
        user = value.usuario
        if not user == self.user:
            raise ValidationError(
                _('La dirección no es dirección del %(role)s'),
                params={ 'role': self.role },
            )