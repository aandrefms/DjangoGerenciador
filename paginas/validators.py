import os
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Construir uma função verificadora em algum campo
def validate_foto(value):
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_comprovante(value):
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def verify_cpf(cpf):
    validator = '^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$'
    if re.match(validator, cpf) is None:
        raise ValidationError(
            _('%(value)s nao eh um cpf valido'),
            params={'value': cpf},
        )