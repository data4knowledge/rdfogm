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

    def add(self, new_value):
        if isinstance(new_value, PropertyLiteral):
            super(self).add(new_value)
        else:
            raise DataPropertyError(f"Error adding a value for a data property. Invalid class {type(new_value)}.")

