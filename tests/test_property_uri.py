import pytest

from rdfogm.property_uri import PropertyUri

def test_initial_state():
    value = PropertyUri("XXX")
    assert value.__str__() == "XXX"

def test_initial_state_empty():
    value = PropertyUri("")
    assert value.__str__() == ""

def test_to_id():
    value = PropertyUri("http://www.example.com#A").to_id()
    assert value == "aHR0cDovL3d3dy5leGFtcGxlLmNvbSNB"
    
def test_from_id():
    value = PropertyUri.from_id("aHR0cDovL3d3dy5leGFtcGxlLmNvbSNB")
    assert value == PropertyUri("http://www.example.com#A")
