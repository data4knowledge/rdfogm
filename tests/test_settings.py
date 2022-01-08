import pytest

from rdfogm.settings import Settings

def test_defaults():
    settings = Settings()
    assert settings.triple_store_protocol == "http"
    assert settings.triple_store_host == "localhost"
    assert settings.triple_store_port == "3030"
    assert settings.triple_store_dataset == "test"

def test_graph():
    settings = Settings()
    assert settings.default_graph == "http://www.data4knowledge/graphs/test"

def test_graph():
    settings = Settings()
    assert settings.rdf_types['http://www.example.com/A'] == 'ModelName'
