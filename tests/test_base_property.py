import pytest

from rdfogm.base_property import BaseProperty
from rdflib.term import URIRef

def test_setting_name():
    params = {'name': 'Jack'}
    property = BaseProperty(**params)
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.default == ""
    assert property.datatype == URIRef("http://www.w3.org/2001/XMLSchema#string")
    assert property.klass == None
    assert property.read_path == False
    assert property.delete_path == False
    assert property.export_path == False

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

def test_setting_default_set():
    params = {'name': 'Jack', 'default': 'xxx'}
    property = BaseProperty(**params)
    assert property.name == "Jack"
    assert property.default == "xxx"
