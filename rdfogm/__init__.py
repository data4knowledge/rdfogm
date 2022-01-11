from rdflib import Graph, Literal
from rdfogm.data_property import DataProperty
from rdfogm.object_property import ObjectProperty
from rdfogm.rdf_type_property import RdfTypeProperty
from rdfogm.property_uri import PropertyUri
from rdfogm.connection import Connection
from rdfogm.settings import Settings

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        properties = dict()
        predicates = dict()
        for k, v in attrs.items():
            if isinstance(v, DataProperty) or isinstance(v, ObjectProperty) or isinstance(v, RdfTypeProperty):
                properties[k] = v
        for k, v in properties.items():
            attrs.pop(k)
            predicates[v.predicate.__str__] = v
        settings = Settings()
        attrs['__properties__'] = properties 
        attrs['__predicates__'] = predicates
        attrs['uri'] = None
        attrs['__new_record__'] = True
        attrs['__destroyed__'] = False
        attrs['__connection__'] = Connection(PropertyUri(settings.default_graph))
        attrs['__triples__'] = []
        return type.__new__(cls, name, bases, attrs)

class Model(object, metaclass=ModelMetaclass):

    CREATE_OP = 'create'
    UPDATE_OP = 'update'

    def __init__(self, **kw):
        for name, value in kw.items():
            setattr(self, name, value)
        setattr(self, '__triples__', [])

    def __getattr__(self, key):
        try:
            if key == "uri":
                return super().__getattr__(key)
            elif self.__properties__[key].has_one():
                return self.__properties__[key].values()
            else:
                return self.__properties__[key]
        except KeyError:
            raise AttributeError(r"A '%s' instance has no attribute named '%s'" % (self.__class__.__name__, key))

    def __setattr__(self, key, value):
        try:
            if key == "uri" or key == "__triples__":
                return super().__setattr__(key, value)
            elif self.__properties__[key].has_one:
                self.__properties__[key].add(value)
            else:
                raise AttributeError(r"Cannot set attribute '%s' directly as it has cardinality of many. Use the add method" % key)
        except KeyError:
            raise AttributeError(r"A '%s' instance has no attribute named '%s'" % (self.__class__.__name__, key))

    def properties(self):
        return self.__properties__

    def triples(self):
        return self.__triples__

    def clear_triples(self):
        self.__triples__ = []

    def is_valid(self, operation):
        return True

    def _is_persisted(self):
        return not(self.__new_record__ or self.__destroyed__)

    def _what_operation(self):
        persisted = self._is_persisted()
        return self.UPDATE_OP if persisted else self.CREATE_OP

    def _create_or_update(self, operation):
        if operation == self.CREATE_OP:
            self.__connection__.temporary_graph()
            for kp, vp in self.__properties__.items():
                for kv, vv in vp.values_as_dict().items():
                    if not vv.to_be_saved:
                        continue
                    vv.saved
                    self.__connection__.add(self.uri, vp.predicate, vv.value)
            self.__connection__.commit()
        else:
            pass

    def save(self):
        operation = self._what_operation()
        if not self.is_valid(operation): return self 
        self._create_or_update(operation)

    @classmethod
    def find(cls, uri_or_id):
        object = None
        settings = Settings()
        connection = Connection(PropertyUri(settings.default_graph))
        uri = cls.__to_uri(uri_or_id)
        result = connection.find(uri)
        print(f"Find: {result}", flush=True)
        for p, o in result:
            print(f"Find: ({p} {o})", flush=True)
            if object == None:
                object = cls()
            try:
                property = object.__predicates__[p.__str__]
                property.add(o)
            except:
                object.__triples__.append((uri, p, o))
        connection = None
        return object

    @classmethod
    def klass_for_uri(cls, uri):
        key = cls.rdf_type(uri)
        try:
          settings = Settings()
          klass = settings.rdf_types[key.__str__()]
          return klass
        except KeyError:
          return None

    @classmethod
    def rdf_type(cls, uri):
        settings = Settings()
        connection = Connection(PropertyUri(settings.default_graph))
        return connection.rdf_type(uri)

    @classmethod
    def __to_uri(cls, uri_or_id):
        return uri_or_id if isinstance(uri_or_id, PropertyUri) else PropertyUri.from_id(uri_or_id)
