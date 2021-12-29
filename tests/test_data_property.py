import pytest

from rdfogm.data_property import DataProperty
from rdfogm.property_literal import PropertyLiteral
from rdflib.term import URIRef

def test_setting_name():
    property = DataProperty(**{'name': 'Jack'})
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.default == ""
    assert property.datatype == URIRef("http://www.w3.org/2001/XMLSchema#string")

def test_setting_cardinality():
    property = DataProperty(**{'name': 'Jack', 'cardinality': 'many'})
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.default == ""
    assert property.datatype == URIRef("http://www.w3.org/2001/XMLSchema#string")
    assert property.cardinality == "many"

def test_add_single_string():
    property = DataProperty(**{'name': 'Jack', 'cardinality': 'one'})
    property.add("A string")
    print(property.values())
    assert property.values() == "A string"

def test_add_single_literal():
    property = DataProperty(**{'name': 'Jack', 'cardinality': 'one'})
    property.add(PropertyLiteral("A string"))
    print(property.values())
    assert property.values() == "A string"

def test_add_single_literal_lang():
    property = DataProperty(**{'name': 'Jack', 'cardinality': 'one'})
    property.add(PropertyLiteral("A string", "de"))
    assert property.values() == PropertyLiteral("A string", "de")

def test_add_multiple():
    property = DataProperty(**{'name': 'Jack', 'cardinality': 'many'})
    property.add("A string", "en")
    property.add("A string", "fr")
    assert property.values() == {'1': PropertyLiteral("A string", "en"), '2': PropertyLiteral("A string", "fr")}

