import pytest

from rdfogm.property_uri import PropertyUri

def test_initial_state():
    value = PropertyUri("XXX")
    assert value.__str__() == "XXX"
    assert value.key() == "XXX"

def test_initial_state_empty():
    value = PropertyUri("")
    assert value.__str__() == ""
