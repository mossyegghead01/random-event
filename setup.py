from setuptools import setup
import re

version = ''
with open('random_event/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

requirements = []
with open('req.txt') as f:
  requirements = f.read().splitlines()

if not version:
    raise RuntimeError('version is not set')

long_desc = ""
with open("README.md", "r") as f:
    long_desc = f.read()

setup(
    name = "Random Event",
    author = "mossyegghead01",
    version = version,
    packages = ['random_event'],
    license = 'MIT',
    description = "A python module made to generate random event at almost random time",
    long_description = long_desc,
    long_description_content_type='text/markdown',
    install_requires = requirements,
    url = 'https://github.com/mossyegghead01/random-event',
    project_urls = {
        "Documentation": "https://random-event.readthedocs.io/en/stable/"
    }
)