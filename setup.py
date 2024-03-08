import sys

from setuptools import setup, find_packages


setup(
    name="my-library",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=False,
    license="MIT",
    description="my-library is not your-library",
    long_description=("A library to exercise how to publish multiple "
                      "versions of the documentation generated with "
                      "Sphinx."),
    author="Daniela Rus Morales",
    author_email="danirus@eml.cc",
    test_suite="dummy",
    zip_safe=True
)
