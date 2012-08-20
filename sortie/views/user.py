"""Views intended for a regular user."""

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from ..api import event, person


@view_config(route_name='user-welcome', renderer='welcome.mako')
@view_config(route_name='user-welcome-error', renderer='welcome.mako')
def welcome(request):
    """Display a welcome page to the user."""
    return dict(name=request.matchdict.get('name'))


@view_config(route_name='user-welcome', request_method='POST')
def do_welcome(request):
    """Validate the name and go to the next step."""
    name = request.POST.get('name')
    if name:
        try:
            p = person.by_name(name)
            return HTTPFound(request.route_path('user-register', id=p.id))
        except Exception as e:
            pass
    return HTTPFound(request.route_path('user-welcome-error', name=name))


@view_config(route_name='user-autocomplete', renderer='json')
def name_autocomplete(request):
    """Return matches from a query string."""
    return [dict(id=p.id, name=' '.join([p.first_name, p.last_name]))
            for p in person.complete(request.GET.get('name'))]
    return [dict(p.iteritems(include=['id', 'first_name', 'last_name']))
            for p in person.complete(request.GET.get('name'))]


@view_config(route_name='user-register', renderer='register.mako')
def register(request):
    """Register to events."""
    person_id = request.matchdict.get('id')

    if person_id:
        try:
            family = person.get_family(int(person_id))
            events = event.get_for_family(family)

            return dict(family=family, events=events)
        except Exception as e:
            raise
            pass

    return HTTPFound(request.route_path('user-welcome'))


@view_config(route_name='user-register', renderer='json',
             request_method='POST')
def do_register(request):
    """Register a person to an event."""
    registered = event.register(event_id=int(request.POST.get('event_id')),
                                person_id=int(request.POST.get('person_id')),
                                active=request.POST.get('active') == 'true')

    return dict(registered=registered)
