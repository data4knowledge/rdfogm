from rdfogm.base_property import BaseProperty
from rdfogm.property_literal import PropertyLiteral
from rdflib import XSD

class DataPropertyError(Exception):
    """Raised when there is an error with a data property."""
    pass

class DataProperty(BaseProperty):

    def __init__(self, **options):
        super().__init__(**options)
        self.default = super().set_value(options, 'default', None)
        self.datatype = super().set_value(options, 'datatype', XSD.string)
        if self.__has_default():
            self.add(self.default) # Setup default value

    def add(self, value, lang=None):
        literal =  value if isinstance(value, PropertyLiteral) else PropertyLiteral(value, lang)
        super().add(literal)

    def values(self):
        if self.has_one():
            literal = super().values()
            return None if literal == None else self.__literal_value(literal)
        else:
            return self.__map_values(super().values())

    def __map_values(self, values):
        return {k: self.__literal_value(v) for k, v in values.items()}   

    def __literal_value(self, literal):
        return literal.value if literal.no_language() else literal

    def __has_default(self):
        return False if self.default == None else True
    
    
