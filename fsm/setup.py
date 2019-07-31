from setuptools import setup
from setuptools import find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fsm_engine',
    version='0.1.0.dev3',
    description='Finite State Machine engine implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages= find_packages(
      exclude=[
        'fsm.core.tests'
      ]
    ),
    install_requires=[],  # Optional
    python_requires='>=3',
    author='Fabio Del Bene',
    author_email='delbio87@gmail.com',
    license='LICENSE.txt',
    url='https://github.com/delbio/py-automata',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/delbio/py-automata/issues',
        'Source': 'https://github.com/delbio/py-automata/',
    },
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
         'Operating System :: OS Independent',
    ],
    keywords= 'sample automata finite state machine engine',  # Optional
)
