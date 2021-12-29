import pytest
#from rdflib import Literal

from rdfogm.object_property import ObjectProperty
from rdflib.term import URIRef

from rdfogm.property_uri import PropertyUri

def test_setting_name():
    property = ObjectProperty(**{'name': 'Jack'})
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.klass == None
    assert property.read_path == False
    assert property.delete_path == False
    assert property.export_path == False
    assert property.cardinality == 'one'

def test_setting_klass_set():
    params = {'name': 'Jack', 'klass': 'CLASS'}
    property = ObjectProperty(**params)
    assert property.name == "Jack"
    assert property.klass == "CLASS"

def test_add_single():
    property = ObjectProperty(**{'name': 'Jack', 'cardinality': 'one'})
    property.add(PropertyUri("http://example.com#A"))
    print(property.values())
    assert property.values() == PropertyUri("http://example.com#A")

def test_add_single_string():
    property = ObjectProperty(**{'name': 'Jack', 'cardinality': 'one'})
    property.add("http://example.com#A")
    print(property.values())
    assert property.values() == PropertyUri("http://example.com#A")

def test_add_multiple():
    property = ObjectProperty(**{'name': 'Jack', 'cardinality': 'many'})
    property.add(PropertyUri("http://example.com#A"))
    property.add(PropertyUri("http://example.com#B"))
    assert property.values() == {'1': PropertyUri("http://example.com#A"), '2': PropertyUri("http://example.com#B")}
