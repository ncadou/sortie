from ..models import Event, Registration

event = Event.inject_api(__name__, as_object=True)
registration = Registration.inject_api(__name__, as_object=True)


def get_for_family(family):
    """Return the events that family members can register to."""
    for person in family:
        if person.children:
            return sorted(accessible_events(person), key=lambda e: e.date)

    return list()


def register(event_id, person_id, active):
    """Register a person to an event."""
    reg = registration.get(event_id=event_id, person_id=person_id)

    if not reg:
        reg = Registration(event_id=event_id, person_id=person_id)

    reg.active = active
    reg.save()

    return active


def accessible_events(person):
    """Return the events a person has access to."""
    if person.student:
        events = person.student.class_.events
    else:
        events = set()
        for child in person.children:
            events |= set(child.student.class_.events)

    return list(events)


def has_access(event, person):
    """Check whether a person has access to an event."""
    return event in accessible_events(person)
