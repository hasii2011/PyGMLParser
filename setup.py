import pathlib
from setuptools import setup
from setuptools import find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="pygmlparser",
    version="1.0.0",
    description="Graph Modeling Language (GML) standalone parser for Python 3.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hasii2011/PyGMLParser",
    packages=find_packages(),
    include_package_data=True
)
