# -*- coding:utf-8 -*-

sdict = {
    'name': 'test-travis',
    'version': '0.0.1',
    'keywords': 'travis',
    'packages': [

    ],
    'zip_safe': False,
    'description': 'test-travis',
    'long_description': 'test-travis',
    'author': 'ni-ning',
    'author_email': 'nining1314@gmail.com',
    'classifiers': [
        'Programming Language :: Python :: 3.7',
    ],
    'include_package_data': True
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if __name__ == '__main__':
    setup(**sdict)
