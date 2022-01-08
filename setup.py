from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'RDF Object Graph Mapper'
LONG_DESCRIPTION = 'A first attempt at an RDF Object Graph Mapper. Very simpe to start with.'

# Setting up
setup(
        name="rdfogm", 
        version=VERSION,
        author="Dave IH",
        author_email="<daveih1664dk@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['rdflib'],
        keywords=['python', 'RDF'],
        tests_require=['pytest'],
        classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
        ],
)