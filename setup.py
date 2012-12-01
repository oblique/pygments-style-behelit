#!/usr/bin/python

from setuptools import setup

setup(
    name = 'pygments-style-behelit',
    version = '0.1',
    description = 'Pygments version of the "behelit" theme.',
    license = 'BSD',

    author = 'oblique',
    author_email = 'psyberbits@gmail.com',

    url = 'https://github.com/oblique/pygments-style-behelit',

    packages = ['pygments_style_behelit'],
    install_requires = ['pygments >= 1.4'],

    entry_points = '''[pygments.styles]
                      behelit = pygments_style_behelit:BehelitStyle''',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
