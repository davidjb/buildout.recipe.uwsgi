# coding: utf-8
from setuptools import setup, find_packages
import codecs
setup(
    name="buildout.recipe.uwsgi",
    version="0.1.1",
    description="Buildout recipe for downloading, compiling and configuring uWSGI",
    long_description = codecs.open("README.rst", encoding="utf-8").read(),
    author="Cosmin Luță",
    author_email="q4break@gmail.com",
    license="BSD",
    url="http://github.com/lcosmin/buildout.recipe.uwsgi",
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=["buildout"],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "zc.recipe.egg",
        "setuptools"
    ],
    zip_safe=False,
    entry_points={"zc.buildout": ["default = buildout.recipe.uwsgi:UWSGI"]}
)
