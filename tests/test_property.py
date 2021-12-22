import pytest

from rdfogm.property import Property

def test_setting_name():
    property = Property(name = "Jack")
    assert property.name == "Jack"
