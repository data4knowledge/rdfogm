from rdfogm.base_property import BaseProperty
from rdfogm.property_uri import PropertyUri

class ObjectPropertyError(Exception):
    """Raised when there is an error with an object property."""
    pass

class ObjectProperty(BaseProperty):

    def __init__(self, **options):
        super().__init__(**options)
        self.klass = self.set_value(options, 'klass', None)
        self.read_path = self.set_value(options, 'read_path', False)
        self.delete_path = self.set_value(options, 'delete_path', False)
        self.export_path = self.set_value(options, 'export_path', False)

    def add(self, new_value):
        if isinstance(new_value, PropertyUri):
            super(self).add(new_value)
        else:
            raise ObjectPropertyError(f"Error adding a value for an object property. Invalid class {type(new_value)}.")

