#!/usr/bin/env python

from setuptools import setup


setup(
    name='Flask-QiniuStorage',
    version='0.9.2',
    url='https://github.com/csuzhangxc/Flask-QiniuStorage',
    license='MIT',
    author='Zhang Xuecheng',
    author_email='csuzhangxc@gmail.com',
    description='''Qiniu Storage for Falsk.
    Please visit: https://github.com/csuzhangxc/Flask-QiniuStorage''',
    long_description=open('README.rst').read(),
    py_modules=['flask_qiniustorage'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    keywords='qiniu for flask',
    package_data={'': ['LICENSE']},
    install_requires=[
        'setuptools',
        'Flask',
        'qiniu'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)