import pytest

from rdfogm.base_property import BaseProperty, BasePropertyError
from rdfogm.property_uri import PropertyUri
from rdflib.term import URIRef
from rdfogm.property_literal import PropertyLiteral

def test_setting_properties():
    params = {'name': 'Jack'}
    property = BaseProperty(**params)
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.cardinality == "one"

def test_setting_cardinality():
    params = {'name': 'Jack', 'cardinality': 'many'}
    property = BaseProperty(**params)
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.cardinality == "many"

def test_setting_has_many():
    params = {'name': 'Jack', 'cardinality': 'many'}
    property = BaseProperty(**params)
    assert property.has_one() == False
    assert property.has_many() == True

def test_setting_has_one():
    params = {'name': 'Jack', 'cardinality': 'one'}
    property = BaseProperty(**params)
    assert property.has_one() == True
    assert property.has_many() == False

def test_setting_cardinality_error():
    params = {'name': 'Jack', 'cardinality': 'manyXX'}
    property = BaseProperty(**params)
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.cardinality == "one"

def test_setting_extra_ignored():
    params = {'name': 'Jack', 'Something': 'manyXX'}
    property = BaseProperty(**params)
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.cardinality == "one"

def test_setting_name():
    params = {'name': 'Jack'}
    property = BaseProperty(**params)
    assert property.name == "Jack"
    assert property.predicate == "Jack"

def test_setting_predicate_set():
    params = {'name': 'Jack', 'predicate': 'something else'}
    property = BaseProperty(**params)
    assert property.name == "Jack"
    assert property.predicate == "something else"

def test_setting_default_set():
    params = {'name': 'Jack', 'predicate': 'something else'}
    property = BaseProperty(**params)
    assert property.name == "Jack"
    assert property.predicate == "something else"

def test_add_uri():
    params = {'name': 'Jack'}
    property = BaseProperty(**params)
    uri = URIRef("http://www.w3.org/2001/XMLSchema#string")
    property.add(uri)
    assert property.len() == 1
    assert property.values().__str__() == "http://www.w3.org/2001/XMLSchema#string"

def test_add_literal():
    property = BaseProperty(**{'name': 'Jack'})
    literal = PropertyLiteral("A string", "en")
    property.add(literal)
    assert property.len() == 1
    assert property.values().__str__() == PropertyLiteral("A string", "en").__str__()

def test_add_literal_single():
    property = BaseProperty(**{'name': 'Jack'})
    literal = PropertyLiteral("A string", "en")
    property.add(literal)
    assert property.len() == 1
    assert property.values().__str__() == PropertyLiteral("A string", "en").__str__()
    literal = PropertyLiteral("A second string", "en")
    property.add(literal)
    assert property.len() == 1
    assert property.values().__str__() == PropertyLiteral("A second string", "en").__str__()

def test_add_multiple_literal():
    params = {'name': 'Jack', 'cardinality': 'many'}
    property = BaseProperty(**params)
    property.add(PropertyLiteral("A string", "en"))
    property.add(PropertyLiteral("A string", "fr"))
    assert property.len() == 2
    assert property.values()['1'].__str__() == PropertyLiteral("A string", "en").__str__()
    assert property.values()['2'].__str__() == PropertyLiteral("A string", "fr").__str__()

def test_remove_literal():
    params = {'name': 'Jack', 'cardinality': 'many'}
    property = BaseProperty(**params)
    property.add(PropertyLiteral("A string", "en"))
    property.add(PropertyLiteral("A string", "fr"))
    assert property.len() == 2
    property.remove('2')
    assert property.len() == 1
    assert property.values()['1'].__str__() == PropertyLiteral("A string", "en").__str__()

def test_remove_literal_exception():
    params = {'name': 'Jack', 'cardinality': 'many'}
    property = BaseProperty(**params)
    with pytest.raises(BasePropertyError) as excinfo:   
        property.remove('3')
    assert 'Error removing a value for Jack' in str(excinfo.value)

def test_replace_literal():
    params = {'name': 'Jack', 'cardinality': 'many'}
    property = BaseProperty(**params)
    property.add(PropertyLiteral("A string", "en"))
    property.add(PropertyLiteral("A string", "fr"))
    assert property.len() == 2
    property.replace('2', PropertyLiteral("A string", "ge"))
    assert property.len() == 2
    assert property.values()['1'].__str__() == PropertyLiteral("A string", "en").__str__()
    assert property.values()['2'].__str__() == PropertyLiteral("A string", "ge").__str__()

def test_replace_literal_exception():
    params = {'name': 'Jack', 'cardinality': 'many'}
    property = BaseProperty(**params)
    with pytest.raises(BasePropertyError) as excinfo:   
        property.replace('1', PropertyLiteral("A string", "ge"))
    assert 'Error replacing a value for Jack' in str(excinfo.value)
