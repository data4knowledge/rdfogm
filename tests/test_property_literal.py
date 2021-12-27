import pytest

from rdfogm.property_literal import PropertyLiteral
from rdflib.term import URIRef
from rdflib.term import Literal

def test_initial_state():
    value = PropertyLiteral("XXX")
    assert value.__str__() == "XXX"
    assert value.key() == "XXX.None"

def test_initial_state_language():
    value = PropertyLiteral("XXX", "fr")
    assert value.__str__() == "XXX"
    assert value.key() == "XXX.fr"