#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='floranet',
      version = '0.4.0',
      description = 'LoRa Network Server',
      author = 'Frank Edwards',
      author_email = 'frank.edwards@fluentnetworks.com.au',
      url = 'https://github.com/fluentnetworks/floranet',
      packages = find_packages(exclude=["*.test", "*.test.*"]),
      install_requires = ['twisted>=16.1.1,<16.7.0', 'psycopg2>=1.6',
                          'twistar>=1.6', 'alembic>=0.8.8', 
                          'py2-ipaddress>=3.4.1',
                          'pycrypto>=2.6.1', 'CryptoPlus==1.0',
                          'requests>=2.13.0', 'flask>=0.12',
                          'Flask-RESTful>=0.3.5', 'Flask-Login>=0.4.0',
                          'crochet>=1.6.0', 'click>=6.7', 'click_shell>=1.0',
                          'mock>=2.0.0'],
      dependency_links = ['https://github.com/doegox/python-cryptoplus/tarball/master#egg=CryptoPlus-1.0'],
      scripts = ['cmd/floranet', 'cmd/floracmd'],
    )

