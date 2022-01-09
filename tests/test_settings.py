import pytest

from rdfogm.settings import Settings

def test_defaults():
    settings = Settings()
    assert settings.protocol == "http"
    assert settings.host == "localhost"
    assert settings.port == "3030"
    assert settings.dataset == "test"

def test_graph():
    settings = Settings()
    assert settings.default_graph == "http://www.data4knowledge/graphs/test"

def test_graph():
    settings = Settings()
    assert settings.rdf_types['http://www.example.com/A'] == 'ModelName'
