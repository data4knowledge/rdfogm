import pytest
from rdflib.term import URIRef

from rdfogm.property_uri import PropertyUri

def test_initial_state_uri():
    value = PropertyUri("http://www.example.com")
    assert value.__str__() == "http://www.example.com"

def test_initial_state_string():
    uri = URIRef("http://www.example.com")
    value = PropertyUri(uri)
    assert value.__str__() == "http://www.example.com"

def test_initial_state_empty():
    value = PropertyUri("")
    assert value.__str__() == ""

def test_to_id():
    value = PropertyUri("http://www.example.com#A").to_id()
    assert value == "aHR0cDovL3d3dy5leGFtcGxlLmNvbSNB"
    
def test_from_id():
    value = PropertyUri.from_id("aHR0cDovL3d3dy5leGFtcGxlLmNvbSNB")
    assert value == PropertyUri("http://www.example.com#A")
