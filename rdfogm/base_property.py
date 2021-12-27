from rdflib.namespace import XSD

from rdfogm.property_value import PropertyValue

class BasePropertyError(Exception):
    """Raised when there is an error with a property operation."""
    pass

class BaseProperty(object):

    def __init__(self, **options):
        self.name = options['name']
        self.predicate = self.set_value(options, 'predicate', options["name"])
        self.values = {}

    def add(self, new_value):
        try:
            value = PropertyValue(new_value)
            self.values[new_value.key()] = value
        except:
            raise BasePropertyError(f"Error adding a value for {self.name}. Value was {new_value}.")

    def remove(self, old_value):
        try:
            self.values.pop(old_value.key(), None)
        except:
            raise BasePropertyError(f"Error deleting a value for {self.name}. Value was {old_value}.")

    def replace(self, old_value, new_value):
        self.remove(old_value)
        self.add(new_value)

    def values(self):
        return self.values

    def set_value(self, options, name, default):
        if name in options:
            return options[name]
        else:
            return default

    def __repr__(self) -> str:
        return super().__repr__()



