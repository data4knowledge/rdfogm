import pytest
import rdfogm

from rdfogm import Model
from rdfogm.data_property import DataProperty

class Person(Model):
    params = {'name': 'name'}
    name = DataProperty(**params)

    def __init__(self):
        super().__init__()


person = Person()
print(person)
person.name = "Jack"
assert person.name == "Jack"