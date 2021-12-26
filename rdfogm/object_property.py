class ObjectProperty(object):

    def __init__(self, **options):
        self.name = options['name']
        self.predicate = self._key_value(options, 'predicate', options["name"])
        self.klass = self._key_value(options, 'klass', '')
        self.read_path = self._key_value(options, 'read_path', False)
        self.delete_path = self._key_value(options, 'delete_path', False)
        self.export_path = self._key_value(options, 'export_path', False)

    def __repr__(self) -> str:
        return super().__repr__()

    def _key_value(self, options, name, default):
        if name in options:
            return options[name]
        else:
            return default
