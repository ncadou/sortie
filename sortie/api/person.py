from csv import reader
from uuid import uuid4

from ..lib.utils import strip_accents
from ..models import Person, User

Person.inject_api(__name__)


def import_csv(file):
    """Import people from a file-like object in UTF8-encoded CSV format.

    CSV fields:
        first_name, last_name, parent1_first_name, parent1_last_name,
        parent2_first_name, parent2_last_name, address city, state, country,
        postal_code, home_phone, work_phone, cell_phone, email

    The CSV file should not start with a headers row.

    """
    people = dict()
    tmp_pwd = unicode(uuid4())
    field = lambda n: fields[n].decode('utf8') if fields[n] else None

    for fields in reader(file):
        person = Person(first_name=field(0), last_name=field(1),
                        address=field(6), city=field(7), state=field(8),
                        country=field(9), postal_code=field(10),
                        home_phone=field(11), work_phone=field(12),
                        cell_phone=field(13), email=field(14))
        username = str(strip_accents(person.first_name + person.last_name))
        user = User(username=filter(str.isalnum, username), password=tmp_pwd)
        person.user = user

        if person.first_name + person.last_name not in people:
            people[person.first_name + person.last_name] = person

            for parent_name in [str(field(2)) + str(field(3)),
                                str(field(4)) + str(field(5))]:
                if parent_name == 'NoneNone':
                    continue
                if parent_name in people:
                    person.parents.append(people[parent_name])
                else:
                    raise ValueError('Parent "%s" not on file' % parent_name)

    for person in people.values():
        person.save()
