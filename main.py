# We use the __file__ dunder method which returns the current file path, and the built-in Path class to navigate through the directory. 
#We make this package installable by creating the setup.py inside the project folder
from setuptools import setup, find_packages

setup(
    name="project_package",
    packages=find_packages(),
)