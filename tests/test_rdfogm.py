import pytest
import os

from tests.helpers.triple_store import TripleStore
from rdfogm import Model, ObjectProperty, DataProperty, RdfTypeProperty, PropertyUri, Settings

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')

class PersonTest(Model):
    rdf_type = RdfTypeProperty(PropertyUri("http://www.w3.org/TypeX"))
    name = DataProperty(**{'name': 'name', 'cardinality': 'one', 'predicate': PropertyUri("http://www.w3.org/name")})
    surname = DataProperty(**{'name': 'surname', 'cardinality': 'one', 'predicate': PropertyUri("http://www.w3.org/surname")})
    has_default = DataProperty(**{'name': 'has_default', 'cardinality': 'one', 'default': 'xxx', 'predicate': PropertyUri("http://www.w3.org/default")})
    nicknames = DataProperty(**{'name': 'nicknames', 'cardinality': 'many', 'predicate': PropertyUri("http://www.w3.org/nickname")})
    rel = ObjectProperty(**{'name': 'rel', 'predicate': PropertyUri("http://www.w3.org/rel")})
    links = ObjectProperty(**{'name': 'links', 'cardinality': 'many', 'predicate': PropertyUri("http://www.w3.org/links")})

    def __init__(self):
        super().__init__()

class Type1Test(Model):
    rdf_type = RdfTypeProperty(PropertyUri("http://www.w3.org/Type1"))

class Type2Test(Model):
    rdf_type = RdfTypeProperty(PropertyUri("http://www.w3.org/Type2"))

@pytest.fixture(autouse=True)
def run_before_and_after_tests(tmpdir):
    settings = Settings()
    ts = TripleStore()
    ts.clear(settings.default_graph)
    yield
    # Teardown : fill with any logic you want

@pytest.fixture
def test_person():
    person = PersonTest()
    person.name = "Jack"
    person.surname = "Daniel's"
    person.nicknames.add("sid") 
    person.rel = PropertyUri('http://example.com#rel-1') 
    person.links.add(PropertyUri('http://example.com#links-1'))
    person.links.add(PropertyUri('http://example.com#links-2'))
    return person

def test_instance_defaults():
    person = PersonTest()
    assert person.has_default == "xxx"
    assert person.name == None
    assert person.surname == None
    assert person.nicknames.values() == {}
    assert person.rel == None
    assert person.links.values() == {}

def test_instance_property_set():
    person = PersonTest()
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

def test_save_full(test_person):
    test_person.uri = PropertyUri('http://example.com#Subject11')
    test_person.save()

def test_save_partial(test_person):
    test_person.uri = PropertyUri('http://example.com#Subject22')
    test_person.save()
    test_person.surname = "Fred"
    test_person.save()

def test_find(test_person):
    test_person.uri = PropertyUri('http://example.com#Subject33')
    test_person.save()
    uri = PropertyUri('http://example.com#Subject33')
    person = PersonTest.find(uri)
    assert type(person) == PersonTest

def test_cannot_find():
    uri = PropertyUri('http://example.com#Subject44')
    person = PersonTest.find(uri)
    assert person == None

def test_extra_triples():
    ts = TripleStore()
    ts.upload(os.path.join(FIXTURE_DIR, "data-1.ttl"), "http://www.data4knowledge/graphs/test")
    uri = PropertyUri('http://www.data4knowledge/orgs/DUNS123456789')
    person = PersonTest.find(uri)
    assert len(person.triples()) == 7

def test_klass_for_uri():
    ts = TripleStore()
    ts.upload(os.path.join(FIXTURE_DIR, "data-2.ttl"), "http://www.data4knowledge/graphs/test")
    uri = PropertyUri('http://www.data4knowledge/test/Test1')
    klass = Model.klass_for_uri(uri)
    assert klass == 'Type1Test'
    uri = PropertyUri('http://www.data4knowledge/test/Test2')
    klass = Model.klass_for_uri(uri)
    assert klass == 'Type2Test'

def test_rdf_type():
    ts = TripleStore()
    ts.upload(os.path.join(FIXTURE_DIR, "data-2.ttl"), "http://www.data4knowledge/graphs/test")
    uri = PropertyUri('http://www.data4knowledge/test/Test1')
    klass = Model.klass_for_uri(uri)
    assert klass == "Type1Test"
    uri = PropertyUri('http://www.data4knowledge/test/Test1')
    result = eval(klass).find(uri)
    assert len(result.triples()) == 2
