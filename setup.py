from setuptools import setup, find_packages

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='logredactor',
    packages=find_packages(),
    version='0.0.1',
    description='Redact logs based on regex filters',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
