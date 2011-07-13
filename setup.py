import distribute_setup
distribute_setup.use_setuptools()

import os
from setuptools import setup, find_packages

version = '1.0.0b'
README = os.path.join(os.path.dirname(__file__), 'README')
long_description = open(README).read()

setup(
    name='cAST',
    version=version,
    description=long_description,
    author='Scott Frazer',
    author_email='scott.d.frazer@gmail.com',
    packages=['cast'],
    package_dir={'cast': 'cast'},
    entry_points={
      'console_scripts': [
            'cast = cast.Main:Cli'
        ]
      },
    license = "GPL",
    keywords = "C preprocessor and parser",
    url = "http://scottfrazer.net/cast",
    classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Topic :: Software Development :: Compilers"
      ]
    )