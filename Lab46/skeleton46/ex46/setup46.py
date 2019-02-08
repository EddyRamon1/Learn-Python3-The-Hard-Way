try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'EX46',
    'author': 'Eddy Ramon',
    'url': 'https://ide.c9.io/coder02/python-work',
    'download_url': 'https://c9.io/coder02/python-work/files/ex46',
    'author_email': 'student.125897@worcesterschools.net',
    'version': '3.6',
    'install_requires': ['nose'],
    'packages': ['ex46'],
    'scripts': ['bin/script.py'],
    'name': 'skeleton46'
}

setup(**config)