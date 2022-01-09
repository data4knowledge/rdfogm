import pytest
import os

from rdflib import Graph
from tests.helpers.triple_store import TripleStore
from rdfogm import Connection, PropertyUri, Settings

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')

def test_instance():
    connection = Connection(PropertyUri('http://www.data4knowledge/graph'))
    assert connection != None

def test_default_graph():
    connection = Connection(PropertyUri('http://www.data4knowledge/graph'))
    assert isinstance(connection.default_graph(), Graph) == True

def test_find():
    ts = TripleStore()
    ts.upload(os.path.join(FIXTURE_DIR, "data-2.ttl"), "http://www.data4knowledge/graphs/test")
    uri = PropertyUri('http://www.data4knowledge/test/Test1')
    settings = Settings()
    connection = Connection(PropertyUri(settings.default_graph))
    result = connection.find(uri)
    print(result)
#    assert result.__str__() == "http://www.w3.org/Type1"

def test_rdf_type():
    ts = TripleStore()
    ts.upload(os.path.join(FIXTURE_DIR, "data-2.ttl"), "http://www.data4knowledge/graphs/test")
    uri = PropertyUri('http://www.data4knowledge/test/Test1')
    settings = Settings()
    connection = Connection(PropertyUri(settings.default_graph))
    result = connection.rdf_type(uri)
    assert result.__str__() == "http://www.w3.org/Type1"
