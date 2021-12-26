import pytest
#from rdflib import Literal

from rdfogm.data_property import DataProperty
from rdflib.term import URIRef

def test_setting_name():
    params = {'name': 'Jack'}
    property = DataProperty(**params)
    assert property.name == "Jack"

#def test_string_literal():
#    result = DataProperty.string_literal()
#    assert result.datatype == URIRef('http://www.w3.org/2001/XMLSchema#string')
    