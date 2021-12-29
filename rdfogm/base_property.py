from rdflib.namespace import XSD

from rdfogm.property_value import PropertyValue

class BasePropertyError(Exception):
    """Raised when there is an error with a property operation."""
    pass

class BaseProperty(object):

    HAS_ONE_KEY = '1'
    CARDINALITY = ('one', 'many') # First entry is default

    def __init__(self, **options):
        self.name = options['name']
        self.predicate = self.set_value(options, 'predicate', options["name"])
        self.cardinality = self.set_value(options, 'cardinality', self.CARDINALITY[0], self.CARDINALITY)
        self.__values = {}
        self.__next_key = 1

    def add(self, new_value):
        self.__values[str(self.__next_key)] = PropertyValue(new_value)
        print(self.__values)
        if self.has_many(): 
            self.__next_key += 1

    def remove(self, key):
        try:
            self.__values.pop(key)
        except:
            raise BasePropertyError(f"Error removing a value for {self.name}")

    def replace(self, key, new_value):
        try:
            self.__values.pop(key)
            self.__values[key] = PropertyValue(new_value)
        except:
            raise BasePropertyError(f"Error replacing a value for {self.name}")

    def len(self):
        return len(self.__values)

    def values(self):
        return self.__values[self.HAS_ONE_KEY].value if self.has_one() else self.__values

    def set_value(self, options, name, default, permitted=()):
        if name in options:
            if (not permitted) or (permitted and options[name] in permitted):
                return options[name]
            else:
                return default
        else:
            return default

    def has_many(self):
        return False if self.cardinality == self.CARDINALITY[0] else True

    def has_one(self):
        return True if self.cardinality == self.CARDINALITY[0] else False

    def __repr__(self) -> str:
        return super().__repr__()



