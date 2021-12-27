import pytest

from rdfogm.property_value import PropertyValue

def test_initial_state():
    value = PropertyValue()
    assert value.value == None
    assert value.to_be_saved() == False

def test_set():
    value = PropertyValue()
    value.value = "Set"
    assert value.value == "Set"
    assert value.to_be_saved() == True

def test_cleared():
    value = PropertyValue()
    value.value = "Set"
    assert value.to_be_saved() == True
    value.saved()
    assert value.value == "Set"
    assert value.to_be_saved() == False
