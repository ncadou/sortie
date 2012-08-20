from pyramid.events import BeforeRender, NewRequest, subscriber
from pyramid.i18n import get_localizer, TranslationStringFactory
from pyramid.threadlocal import get_current_request

from . import helpers

tsf = TranslationStringFactory('Sortie')


@subscriber(NewRequest)
def add_localizer(event):
    request = event.request
    localizer = get_localizer(request)

    def auto_translate(string):
        return localizer.translate(tsf(string))
    request.localizer = localizer
    request.translate = auto_translate


@subscriber(BeforeRender)
def add_renderer_globals(event):
    """A subscriber to the ``pyramid.events.BeforeRender`` events.  Updates
    the :term:`renderer globals` with values that are familiar to Pylons
    users."""
    request = event.get('request')
    if request is None:
        request = get_current_request()

    globs = dict()

    def _path(*args, **kwargs):
        return request.route_path(*args, **kwargs)

    def _static_path(asset, **kwargs):
        return request.static_path('sortie:static' + asset, **kwargs)

    globs['path'] = _path
    globs['static_path'] = _static_path

    globs['_'] = request.translate
    globs['localizer'] = request.localizer

    globs['h'] = helpers

    event.update(globs)

