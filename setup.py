import os
from distutils.core import setup

# Utility function to read files. Used for the long_description.
def read(fname):
      return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='osdf-python',
      description='Python client to Open Science Data Framework (OSDF) REST servers.',
      long_description=read('README.md'),
      version='0.4',
      py_modules=['osdf', 'request'],
      author='Victor Felix',
      author_email='victor73@github.com',
      url='http://osdf.igs.umaryland.edu',
      license='MIT',
      install_requires=['httplib', 'jsondiff'],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
      ]
     )
