import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-cleanup-later',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A quick, rough around the edges Django application to remember and remove temporary files.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://www.bravasoftware.com/',
    author='Mark Skelton',
    author_email='mark@bravasoftware.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
