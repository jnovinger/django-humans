# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='django-humans',
    version='0.1',
    author=u'Jason Novinger',
    author_email='jnovinger@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/jnovinger/django-humans',
    license='MIT - http://opensource.org/licenses/mit-license.php',
    description='A completely over-engineered Django app to provide /humans.txt.',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
