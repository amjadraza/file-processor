#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="MA Raza",
    author_email='amjadraza24@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A project to processor files",
    entry_points={
        'console_scripts': [
            'file_processor=file_processor.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='file_processor',
    name='file_processor',
    packages=find_packages(include=['file_processor', 'file_processor.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/amjadraza/file_processor',
    version='0.1.0',
    zip_safe=False,
)
