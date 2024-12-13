import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "titulos_2024.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import titulos_2024.users.signals  # noqa: F401
