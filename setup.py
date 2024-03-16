from setuptools import setup, find_packages

setup(
    name='pysqldf',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1.5',
        'sqlite3>=2.6.0',  # sqlite3 is part of the Python standard library
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple function to run SQL queries on pandas DataFrames using SQLite syntax.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
