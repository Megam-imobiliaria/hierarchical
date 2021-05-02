from django.conf import settings
from functools import cached_property
from .apps import SourceApp


class Project:
    @cached_property
    def source_apps(self):
        return SourceApp.collect()

    @cached_property
    def installable_apps(self):
        return SourceApp.discover()

    @cached_property
    def urlpatterns(self):
        from django.conf.urls.static import static

        return [
            app.urlpatterns() for app
            in self.source_apps
            if app.has('urls')
        ] \
            + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


__project__ = Project()
