from setuptools import setup, find_packages
import os

name = 'seantis.templates'
version = '0.1'

description = 'Templates for Seantis Modules based on templer.'
long_description = '\n'.join((
    open('README.rst').read(),
    open(os.path.join('docs', 'HISTORY.txt')).read()
))

classifiers = []
keywords = []

author = 'Seantis GmbH'
author_email = 'info@seantis.ch'
url = 'https://github.com/seantis/seantis.reservation'
license = 'MIT'

install_requires = [
    'templer.core',
    'setuptools',
    'templer.core',
]

entry_points = """
    [paste.paster_create_template]
    seantis_directory = seantis.templates.directory:Directory

    [templer.templer_structure]
    basic = seantis.templates.directory:Basic
"""

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    classifiers=classifiers,
    keywords=' '.join(keywords),
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=name.split('.')[:-1],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points=entry_points
)
