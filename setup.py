import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'alembic',
    'babel',
    'colanderalchemy',
    'cryptacular',
    'lingua',
    'psycopg2',
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'waitress',
    'zope.sqlalchemy',
    ]

setup(name='Sortie',
      version='0.0',
      description='School field trip registration and management app',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='sortie',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = sortie:main
      [console_scripts]
      sortie-db-manage = sortie.scripts.db_manage:main
      sortie-import = sortie.scripts.import:main
      """,
      )

