from rdflib.namespace import XSD

from rdfogm.property_value import PropertyValue

class BasePropertyError(Exception):
    """Raised when there is an error with a property operation."""
    pass

class BaseProperty(object):

    HAS_ONE_KEY = '1'
    CARDINALITY = ('one', 'many')

    def __init__(self, **options):
        self.name = options['name']
        self.predicate = self.set_value(options, 'predicate', options["name"])
        self.cardinality = self.set_value(options, 'cardinality', self.CARDINALITY[0], self.CARDINALITY)
        self.values = {}
        self.next_key = 1

    def add(self, new_value):
        self.values[str(self.next_key)] = PropertyValue(new_value)
        if self.has_many(): 
            self.next_key += 1

    def remove(self, key):
        try:
            self.values.pop(key)
        except:
            raise BasePropertyError(f"Error removing a value for {self.name}.")

    def replace(self, key, new_value):
        try:
            self.values.pop(key)
            self.values[key] = PropertyValue(new_value)
        except:
            raise BasePropertyError(f"Error replacing a value for {self.name}.")

    def values(self):
        return self.values[self.HAS_ONE_KEY] if self.has_obe else self.values

    def set_value(self, options, name, default, permitted=()):
        if name in options:
            if (not permitted) or (permitted and options[name] in permitted):
                return options[name]
            else:
                return default
        else:
            return default

    def has_many(self):
        return False if self.cardinality == 'one' else True

    def has_one(self):
        return True if self.cardinality == 'one' else False

    def __repr__(self) -> str:
        return super().__repr__()



