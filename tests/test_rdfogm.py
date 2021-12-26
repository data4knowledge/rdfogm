import pytest
import rdfogm

from rdfogm import Model
from rdfogm.data_property import DataProperty

def test_rdfogm():

    class Person(Model):
        params = {'name': 'name'}
        name = DataProperty(**params)
        surname = DataProperty(**{'name': 'surname'})

        def __init__(self):
            super().__init__()


    person = Person()
    print(person)
    person.name = "Jack"
    person.surname = "Daniel's"
    assert person.name == "Jack"
    assert person.surname == "Daniel's"

