from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Yaratilgan vaqt"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Yangilangan vaqt"), auto_now=True)

    class Meta:
        abstract = True


class CarModel(BaseModel):
    title = models.CharField(_("Nomi"), max_length=128)

    class Meta:
        verbose_name = _("Mashina modeli")
        verbose_name_plural = _("Mashina modellari")
