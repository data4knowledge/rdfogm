import pytest
import rdfogm

from rdflib import URIRef, Literal
from rdfogm import Model, ObjectProperty, DataProperty, RdfTypeProperty, PropertyUri

class TestPerson(Model):
    rdf_type = RdfTypeProperty(PropertyUri("http://www.w3.org/TypeX"))
    name = DataProperty(**{'name': 'name', 'cardinality': 'one', 'predicate': PropertyUri("http://www.w3.org/name")})
    surname = DataProperty(**{'name': 'surname', 'cardinality': 'one', 'predicate': PropertyUri("http://www.w3.org/surname")})
    has_default = DataProperty(**{'name': 'has_default', 'cardinality': 'one', 'default': 'xxx', 'predicate': PropertyUri("http://www.w3.org/default")})
    nicknames = DataProperty(**{'name': 'nicknames', 'cardinality': 'many', 'predicate': PropertyUri("http://www.w3.org/nickname")})
    rel = ObjectProperty(**{'name': 'rel', 'predicate': PropertyUri("http://www.w3.org/rel")})
    links = ObjectProperty(**{'name': 'links', 'cardinality': 'many', 'predicate': PropertyUri("http://www.w3.org/links")})

    def __init__(self):
        super().__init__()

def test_instance_defaults():
    person = TestPerson()
    assert person.has_default == "xxx"
    assert person.name == None
    assert person.surname == None
    assert person.nicknames.values() == {}
    assert person.rel == None
    assert person.links.values() == {}

def test_instance_property_set():
    person = TestPerson()
    person.name = "Jack"
    person.surname = "Daniel's"
    person.nicknames.add("sid") 
    person.rel = PropertyUri('http://example.com#AS1') 
    person.links.add(PropertyUri('http://example.com#AS2'))
    assert person.name == "Jack"
    assert person.surname == "Daniel's"
    assert person.nicknames.values()['1'] == "sid"
    assert person.rel == PropertyUri('http://example.com#AS1') 
    assert person.links.values()['1'] == PropertyUri('http://example.com#AS2') 

def test_save_full():
    person = TestPerson()
    person.uri = PropertyUri('http://example.com#Subject11')
    person.name = "Jack"
    person.surname = "Daniel's"
    person.nicknames.add("sid") 
    person.rel = PropertyUri('http://example.com#rel-1') 
    person.links.add(PropertyUri('http://example.com#links-1'))
    person.links.add(PropertyUri('http://example.com#links-2'))
    person.save()

def test_save_partial():
    person = TestPerson()
    person.uri = PropertyUri('http://example.com#Subject22')
    person.name = "Jack"
    person.save()
    person.surname = "Fred"
    person.save()

def test_find():
    uri = PropertyUri('http://www.data4knowledge.dk/ms/test-data-2')
    person = TestPerson.find(uri)
    assert type(person) == TestPerson

def test_cannot_find():
    uri = PropertyUri("http://dbpedia.org/resource/Asturias")
    person = TestPerson.find(uri)
    assert person == None

def test_extra_triples():
    uri = PropertyUri('http://www.data4knowledge.dk/ms/test-data-2')
    person = TestPerson.find(uri)
    print(len(person.triples()))
    assert len(person.triples()) == 5



