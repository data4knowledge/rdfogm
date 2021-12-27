import pytest
import rdfogm

from rdflib import URIRef, Literal
from rdfogm import Model
from rdfogm.data_property import DataProperty

class Person(Model):
    name = DataProperty(**{'name': 'name'})
    surname = DataProperty(**{'name': 'surname'})

    def __init__(self):
        super().__init__()

def test_instance_no_params():
    person = Person()
    person.name = "Jack"
    person.surname = "Daniel's"
    assert person.name == "Jack"
    assert person.surname == "Daniel's"

def test_save_full():
    person = Person()
    person.name = "Jack"
    person.surname = "Daniel's"
    person.save

def test_save_partial():
    uri = URIRef("http://dbpedia.org/resource/Asturias")
    person = Person.find(uri)
    person.name = "Jack Updated"
    person.save

def test_find():
    uri = URIRef("http://dbpedia.org/resource/Asturias")
    person = Person.find(uri)

def test_cannot_find():
    uri = URIRef("http://dbpedia.org/resource/Asturias")
    person = Person.find(uri)

def test_extra_triples():
    uri = URIRef("http://dbpedia.org/resource/Asturias")
    person = Person.find(uri)




