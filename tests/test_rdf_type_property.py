import pytest

from rdfogm import RdfTypeProperty, PropertyUri
from rdflib import RDF

def test_setting_name():
    property = RdfTypeProperty(PropertyUri("http://www.w3.org/TypeX"))
    assert property.name == "rdf_type"
    assert property.predicate == RDF.type
    assert property.len() == 1
    assert property.values() == PropertyUri("http://www.w3.org/TypeX")
