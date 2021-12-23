import pytest
#from rdflib import Literal

from rdfogm.data_property import DataProperty

def test_setting_name():
    params = {'name': 'Jack'}
    property = DataProperty(**params)
    assert property.name == "Jack"

def test():
    params = {'name': 'Jack'}
    property = DataProperty(**params)
    property.test
    assert property.name == "Jack"
    