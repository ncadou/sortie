from csv import reader
from uuid import uuid4

from ..lib.utils import strip_accents
from ..models import Class, Person, Student, User

Person.inject_api(__name__)


def by_name(name):
    """Get a person by name."""
    return Person.by_name(name)


def complete(name):
    """Return poor man's possible matches from the provided name."""
    return Person.complete(name)


def get_family(person_id):
    """Return all family members for a person_id."""
    p = Person.get(id=person_id)

    if p.children:
        children = p.children
        parents = children[0].parents
    else:
        parents = p.parents
        children = parents[0].children

    return children + parents


def import_csv(file):
    """Import people from a file-like object in UTF8-encoded CSV format.

    CSV fields:
        first_name, last_name, parent1_first_name, parent1_last_name,
        parent2_first_name, parent2_last_name, class, address city, state,
        country, postal_code, home_phone, work_phone, cell_phone, email

    The CSV file should not start with a headers row.

    """
    people = dict()
    classes = dict()
    students = list()
    tmp_pwd = unicode(uuid4())

    field = lambda n: fields[n].decode('utf8') if fields[n] else None

    for fields in reader(file):
        person = Person(first_name=field(0), last_name=field(1),
                        address=field(7), city=field(8), state=field(9),
                        country=field(10), postal_code=field(11),
                        home_phone=field(12), work_phone=field(13),
                        cell_phone=field(14), email=field(15))
        username = str(strip_accents(person.first_name + person.last_name))
        user = User(username=filter(str.isalnum, username), password=tmp_pwd)
        person.user = user

        if person.first_name + person.last_name not in people:
            people[person.first_name + person.last_name] = person

            for parent_name in [(field(2), field(3)), (field(4), field(5))]:
                if parent_name[0] is None or parent_name[1] is None:
                    continue
                else:
                    parent_name = ''.join(parent_name)

                if parent_name in people:
                    person.parents.append(people[parent_name])
                else:
                    raise ValueError('Parent "%s" not on file' % parent_name)

            class_name = field(6)

            if class_name:
                if class_name not in classes:
                    classes[class_name] = Class.get(name=class_name) or \
                                              Class(name=class_name)
                student = Student(class_=classes[class_name], person=person)
                students.append(student)

    for student in students:
        student.save()

    for person in people.values():
        person.save()
