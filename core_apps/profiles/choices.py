from django.utils.translation import gettext_lazy as _

FEMALE: str = 'FEMALE'
MALE: str = 'MALE'
OTHER: str= 'OTHER'

GENDER: list = [
   (FEMALE, _("FEMALE")),
   (MALE, _("MALE")),
   (OTHER, _("OTHER")),
]