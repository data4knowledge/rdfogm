import pytest

from rdfogm.property_literal import PropertyLiteral
from rdflib.term import URIRef
from rdflib.term import Literal

def test_initial_state():
    value = PropertyLiteral("XXX")
    assert value.__str__() == "XXX"

def test_initial_state_language():
    value = PropertyLiteral("XXX", "fr")
    assert value.__str__() == "XXX"

def test_has_language():
    value = PropertyLiteral("XXX", "fr")
    assert value.has_language() == True
    assert value.no_language() == False

def test_no_language():
    value = PropertyLiteral("XXX")
    assert value.has_language() == False
    assert value.no_language() == True
