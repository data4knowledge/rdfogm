import pytest

from rdfogm.base_property import BaseProperty
from rdfogm.property_uri import PropertyUri
from rdfogm.property_literal import PropertyLiteral

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
    params = {'name': 'Jack', 'default': 'xxx'}
    property = BaseProperty(**params)
    property.add(PropertyUri("http://www.w3.org/2001/XMLSchema#string"))
    assert len(property.values) == 1
    assert property.values['http://www.w3.org/2001/XMLSchema#string'].__str__() == "http://www.w3.org/2001/XMLSchema#string"

def test_add_literal():
    property = BaseProperty(**{'name': 'Jack', 'default': 'xxx'})
    literal = PropertyLiteral("A string", "en")
    property.add(literal)
    assert len(property.values) == 1
    assert property.values['A string.en'].__str__() == PropertyLiteral("A string", "en").__str__()

def test_add_multiple_literal():
    params = {'name': 'Jack', 'default': 'xxx'}
    property = BaseProperty(**params)
    property.add(PropertyLiteral("A string", "en"))
    property.add(PropertyLiteral("A string", "fr"))
    assert len(property.values) == 2
    assert property.values['A string.en'].__str__() == PropertyLiteral("A string", "en").__str__()
    assert property.values['A string.fr'].__str__() == PropertyLiteral("A string", "fr").__str__()

def test_remove_literal():
    params = {'name': 'Jack', 'default': 'xxx'}
    property = BaseProperty(**params)
    property.add(PropertyLiteral("A string", "en"))
    property.add(PropertyLiteral("A string", "fr"))
    assert len(property.values) == 2
    property.remove(PropertyLiteral("A string", "fr"))
    assert len(property.values) == 1
    assert property.values['A string.en'].__str__() == PropertyLiteral("A string", "en").__str__()

def test_replace_literal():
    params = {'name': 'Jack', 'default': 'xxx'}
    property = BaseProperty(**params)
    property.add(PropertyLiteral("A string", "en"))
    property.add(PropertyLiteral("A string", "fr"))
    assert len(property.values) == 2
    property.replace(PropertyLiteral("A string", "fr"), PropertyLiteral("A string", "ge"))
    assert len(property.values) == 2
    assert property.values['A string.en'].__str__() == PropertyLiteral("A string", "en").__str__()
    assert property.values['A string.ge'].__str__() == PropertyLiteral("A string", "ge").__str__()
