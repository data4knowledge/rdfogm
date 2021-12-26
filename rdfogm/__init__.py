from rdfogm.data_property import DataProperty
from rdflib import Graph, Literal

print("RDFOGM 1:")

class ModelType(type):

    def __new__(cls, name, bases, attributes):
        print(cls)
        print(name)
        print(bases)
        print(attributes)

def metaclass(mcs):
    def _metaclass(cls):
        name = cls.__name__
        body = cls.__dict__.copy()
        bases = cls.__bases__
        return mcs(name, bases, body)
    return _metaclass

@metaclass(ModelType)
class Model(object):

    def __init__(self): #, *values, **properties):
        print(self)
        #print(*values)
        #print(**properties)

print("RDFOGM 2: ", Model)

