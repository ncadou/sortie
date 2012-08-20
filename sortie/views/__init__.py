"""App URL routing and renderers are configured here."""


def includeme(config):
    """Initialize views and renderers at app start-up time. """
    config.add_static_view('static', 'sortie:static', cache_max_age=3600)
    config.add_route('user-welcome', 'welcome')
    config.add_route('user-welcome-error', 'welcome/{name}')
    config.add_route('user-autocomplete', 'autocomplete/name')
    config.add_route('user-register', 'register/{id}')

    config.include(auth_urls, route_prefix='/auth')


def auth_urls(config):
    pass
