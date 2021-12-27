import pytest

from rdfogm.property_literal import PropertyLiteral
from rdfogm.property_uri import PropertyUri
from rdfogm.property_value import PropertyValue

def test_initial_state():
    value = PropertyValue()
    assert value.value == None
    assert value.to_be_saved() == False

def test_initial_state_value():
    value = PropertyValue(PropertyLiteral("New"))
    assert value.value == PropertyLiteral("New")
    assert value.to_be_saved() == True

def test_set():
    value = PropertyValue()
    value.value = PropertyLiteral("Set")
    assert value.value == PropertyLiteral("Set")
    assert value.to_be_saved() == True

def test_cleared():
    value = PropertyValue()
    value.value = "Set"
    assert value.to_be_saved() == True
    value.saved()
    assert value.value == "Set"
    assert value.to_be_saved() == False

def test_str_literal():
    value = PropertyValue(PropertyLiteral("YYY"))
    assert value.__str__() == 'YYY'

def test_str_uri():
    uri = PropertyUri("http://example.com#A")
    value = PropertyValue(uri)
    assert value.__str__() == 'http://example.com#A'

