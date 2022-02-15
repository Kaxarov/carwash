from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from common.models import BaseModel
from .managers import UserManager
from .validators import username_validators


class RoleChoices(models.TextChoices):
    admin = "admin", _("Admin")
    worker = "worker", _("Worker")


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    USERNAME_FIELD = "username"
    objects = UserManager()

    full_name = models.CharField(_("Full name"), max_length=128, blank=True, null=True)
    role = models.CharField(
        _("Role"),
        choices=RoleChoices.choices,
        default=RoleChoices.worker,
        max_length=16,
    )
    username = models.CharField(
        _("Username"),
        max_length=128,
        unique=True,
        validators=username_validators,
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
