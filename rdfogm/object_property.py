from rdfogm.base_property import BaseProperty

class ObjectProperty(BaseProperty):

    def __init__(self, **options):
        super().__init__(**options)
        self.klass = self._key_value(options, 'klass', None)
        self.read_path = self._key_value(options, 'read_path', False)
        self.delete_path = self._key_value(options, 'delete_path', False)
        self.export_path = self._key_value(options, 'export_path', False)
