try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'EX48',
    'author': 'Eddy Ramon',
    'url': 'https://ide.c9.io/coder02/python-work',
    'download_url': 'https://c9.io/coder02/python-work/files/ex48',
    'author_email': 'student.125897@worcesterschools.net',
    'version': '3.6',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': ['bin/script.py'],
    'name': 'skeleton48'
}

setup(**config)