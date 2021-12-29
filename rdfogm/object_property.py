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

    def add(self, value):
        super().add(PropertyUri(value))

    def values():
        return super().values()

