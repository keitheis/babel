#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2007 Edgewall Software
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://babel.edgewall.org/wiki/License.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at http://babel.edgewall.org/log/.

import doctest
from glob import glob
import os
from setuptools import find_packages, setup, Command
import sys


class build_doc(Command):
    description = 'Builds the documentation'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from docutils.core import publish_cmdline
        docutils_conf = os.path.join('doc', 'docutils.conf')
        epydoc_conf = os.path.join('doc', 'epydoc.conf')

        for source in glob('doc/*.txt'):
            dest = os.path.splitext(source)[0] + '.html'
            if not os.path.exists(dest) or \
                   os.path.getmtime(dest) < os.path.getmtime(source):
                print 'building documentation file %s' % dest
                publish_cmdline(writer_name='html',
                                argv=['--config=%s' % docutils_conf, source,
                                      dest])

        try:
            from epydoc import cli
            old_argv = sys.argv[1:]
            sys.argv[1:] = [
                '--config=%s' % epydoc_conf,
                '--no-private', # epydoc bug, not read from config
                '--simple-term',
                '--verbose'
            ]
            cli.cli()
            sys.argv[1:] = old_argv

        except ImportError:
            print 'epydoc not installed, skipping API documentation.'


class test_doc(Command):
    description = 'Tests the code examples in the documentation'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for filename in glob('doc/*.txt'):
            print 'testing documentation file %s' % filename
            doctest.testfile(filename, False, optionflags=doctest.ELLIPSIS)


setup(
    name = 'Babel',
    version = '0.1',
    description = 'Internationalization utilities',
    long_description = \
"""A collection of tools for internationalizing Python applications.""",
    author = 'Edgewall Software',
    author_email = 'info@edgewall.org',
    license = 'BSD',
    url = 'http://babel.edgewall.org/',
    download_url = 'http://babel.edgewall.org/wiki/Download',
    zip_safe = False,

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(exclude=['tests']),
    package_data = {'babel': ['localedata/*.dat']},
    test_suite = 'babel.tests.suite',

    entry_points = """
    [console_scripts]
    pygettext = babel.catalog.frontend:main
    
    [distutils.commands]
    extract_messages = babel.catalog.frontend:extract_messages
    
    [babel.extractors]
    genshi = babel.catalog.extract:extract_genshi
    python = babel.catalog.extract:extract_python
    """,

    cmdclass = {'build_doc': build_doc, 'test_doc': test_doc}
)