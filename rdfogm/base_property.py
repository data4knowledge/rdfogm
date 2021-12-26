from rdflib.namespace import XSD

class BaseProperty(object):

    def __init__(self, **options):
        self.name = options['name']
        self.predicate = self._key_value(options, 'predicate', options["name"])
        self.default = self._key_value(options, 'default', '')
        self.datatype = self._key_value(options, 'datatype', XSD.string)
        self.klass = None
        self.read_path = False
        self.delete_path = False
        self.export_path = False

    def __repr__(self) -> str:
        return super().__repr__()

    def _key_value(self, options, name, default):
        if name in options:
            return options[name]
        else:
            return default
