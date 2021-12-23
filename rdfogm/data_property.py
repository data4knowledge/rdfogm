from rdflib import Graph, Literal
from rdflib.namespace import XSD

class DataProperty(object):

    def __init__(self, **options):
        self.name = options['name']
        self.predicate = self._key_value(options, 'predicate', options["name"])
        self.default = self._key_value(options, 'default', '')
        self.datatype = self._key_value(options, 'datatype', 'string')

    @staticmethod
    def string_literal():
        print("1")
        literal = Literal(DataProperty, datatype=XSD.string)
        print(literal)
        print("2")
        return literal
 
    def __repr__(self) -> str:
        return super().__repr__()

    def _key_value(self, options, name, default):
        if name in options:
            return options[name]
        else:
            return default
