import pytest
import rdfogm

from rdflib import URIRef, Literal
from rdfogm import Model, DataProperty, RdfTypeProperty, PropertyUri

class TestPerson(Model):
    rdf_type = RdfTypeProperty(PropertyUri("http://www.w3.org/TypeX"))
    name = DataProperty(**{'name': 'name', 'cardinality': 'one'})
    surname = DataProperty(**{'name': 'surname', 'cardinality': 'one'})
    nicknames = DataProperty(**{'name': 'surname', 'cardinality': 'many'})

    def __init__(self):
        super().__init__()

def test_instance_no_params():
    person = TestPerson()
    person.name = "Jack"
    person.surname.add("Daniel's")
    assert person.name == "Jack"
    assert person.surname == "Daniel's"

def test_save_full():
    person = TestPerson()
    person.name = "Jack"
    person.surname = "Daniel's"
    #assert 0
    person.save()

def test_save_partial():
    uri = URIRef("http://dbpedia.org/resource/Asturias")
    person = TestPerson.find(uri)
    person.name = "Jack Updated"
    person.save()

def test_find():
    uri = URIRef("http://dbpedia.org/resource/Asturias")
    person = TestPerson.find(uri)

def test_cannot_find():
    uri = URIRef("http://dbpedia.org/resource/Asturias")
    person = TestPerson.find(uri)

def test_extra_triples():
    uri = URIRef("http://dbpedia.org/resource/Asturias")
    person = TestPerson.find(uri)




