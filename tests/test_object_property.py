import pytest
#from rdflib import Literal

from rdfogm.object_property import ObjectProperty
from rdflib.term import URIRef

def test_setting_name():
    property = ObjectProperty(**{'name': 'Jack'})
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.default == ""
    assert property.datatype == URIRef("http://www.w3.org/2001/XMLSchema#string")
    assert property.klass == None
    assert property.read_path == False
    assert property.delete_path == False
    assert property.export_path == False

def test_setting_klass_set():
    params = {'name': 'Jack', 'klass': 'CLASS'}
    property = ObjectProperty(**params)
    assert property.name == "Jack"
    assert property.klass == "CLASS"
