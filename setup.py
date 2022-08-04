#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-confd-playagentnumber',
    version='0.1',
    description='Connectino playagentnumber plugin',
    author='Farhad K',
    author_email='foo@bar.com',
    packages=find_packages(),
    url='https://www.foo-bar.com',
    include_package_data=True,
    package_data={
        'wazo_confd_playagentnumber': ['api.yml'],
    },
    entry_points={
        'wazo_confd.plugins': [
            'playagentnumber = wazo_confd_playagentnumber.plugin:Plugin'
        ]
    }
)
