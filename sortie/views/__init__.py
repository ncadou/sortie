"""App URL routing and renderers are configured here."""


def includeme(config):
    """Initialize views and renderers at app start-up time. """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include(auth_urls, route_prefix='/auth')


def auth_urls(config):
    pass
