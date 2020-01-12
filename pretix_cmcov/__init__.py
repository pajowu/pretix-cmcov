from django.utils.translation import ugettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    name = "pretix_cmcov"
    verbose_name = "Customisable Multi-Column Order View"

    class PretixPluginMeta:
        name = ugettext_lazy("Customisable Multi-Column Order View")
        author = "Karl Engelhardt"
        description = ugettext_lazy("Show orders with custom columns")
        visible = True
        version = "1.0.0"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = "pretix_cmcov.PluginApp"
