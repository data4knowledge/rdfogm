import pytest
#from rdflib import Literal

from rdfogm.data_property import DataProperty
from rdflib.term import URIRef

def test_setting_name():
    property = DataProperty(**{'name': 'Jack'})
    assert property.name == "Jack"
    assert property.predicate == "Jack"
    assert property.default == ""
    assert property.datatype == URIRef("http://www.w3.org/2001/XMLSchema#string")
