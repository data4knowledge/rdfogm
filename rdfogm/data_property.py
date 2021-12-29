from rdfogm.base_property import BaseProperty
from rdfogm.property_literal import PropertyLiteral
from rdflib import XSD

class DataPropertyError(Exception):
    """Raised when there is an error with a data property."""
    pass

class DataProperty(BaseProperty):

    def __init__(self, **options):
        super().__init__(**options)
        self.default = super().set_value(options, 'default', '')
        self.datatype = super().set_value(options, 'datatype', XSD.string)

    def add(self, value, lang=None):
        super().add(PropertyLiteral(value, lang))

    def values(self):
        return super().values()
        
