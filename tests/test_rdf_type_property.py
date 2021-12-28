import pytest

from rdfogm import RdfTypeProperty, PropertyUri
from rdflib import RDF

def test_setting_name():
    property = RdfTypeProperty(PropertyUri("http://www.w3.org/TypeX"))
    assert property.name == "rdf_type"
    assert property.predicate == RDF.type
    assert len(property.values) == 1
    assert property.values['http://www.w3.org/TypeX'].value == PropertyUri("http://www.w3.org/TypeX")
