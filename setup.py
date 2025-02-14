# -*- coding: utf8 -*-
from setuptools import setup, find_packages, Command
import os, sys

# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class RunTests(Command):
    description = "Run the django test suite from the testproj dir."

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        this_dir = os.getcwd()
        testproj_dir = os.path.join(this_dir, "test_project")
        os.chdir(testproj_dir)
        sys.path.append(testproj_dir)
        from django.core.management import execute_from_command_line
        os.environ["DJANGO_SETTINGS_MODULE"] = 'test_project.settings'
        settings_file = os.environ["DJANGO_SETTINGS_MODULE"]
        settings_mod = __import__(settings_file, {}, {}, [''])
        execute_from_command_line(argv=[ __file__, "test",
            "session_security"])
        os.chdir(this_dir)

if 'sdist' in sys.argv:
    dir = os.getcwd()
    os.chdir(os.path.join(dir, 'session_security'))
    os.system('django-admin.py compilemessages')
    os.chdir(dir)


setup(
    name='django-session-security',
    version='2.6.7-rc2',
    description='Client and server side session timeout with warnings',
    author='∞',
    author_email='yourlabs@googlegroups.com',
    url='https://github.com/yourlabs/django-session-security',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.rst'),
    license = 'MIT',
    keywords = 'django session',
    cmdclass={'test': RunTests},
    install_requires=[
        'django',
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
