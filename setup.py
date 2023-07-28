from setuptools import setup
from Cython.Build import cythonize

ext_modules = cythonize("print_number_using_cython.pyx")

setup(
    ext_modules=ext_modules
)
