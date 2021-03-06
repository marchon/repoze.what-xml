# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008-2009, 2011, Gustavo Narea <me@gustavonarea.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
version = open(os.path.join(here, 'VERSION.txt')).readline().rstrip()

setup(name='repoze.what.plugins.xml',
      version=version,
      description=('The repoze.what XML plugin'),
      long_description=README,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Security",
        "Topic :: Text Processing :: Markup :: XML",
        ],
      keywords='web application server wsgi xml authorization repoze',
      author="Gustavo Narea",
      author_email="repoze-dev@lists.repoze.org",
      namespace_packages = ['repoze', 'repoze.what', 'repoze.what.plugins'],
      url="http://what.repoze.org/docs/plugins/xml/",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require=['repoze.what', 'coverage', 'nose'],
      install_requires=['repoze.what >= 1.0.1'],
      test_suite="nose.collector",
      entry_points = """\
      """
      )

