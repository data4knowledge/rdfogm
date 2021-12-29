from rdflib import Graph, Literal
from rdfogm.data_property import DataProperty
from rdfogm.object_property import ObjectProperty
from rdfogm.rdf_type_property import RdfTypeProperty
from rdfogm.property_uri import PropertyUri

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        print("A", cls)
        print("A", name)
        print("A", bases)
        print("A", attrs)
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        properties = dict()
        for k, v in attrs.items():
            if isinstance(v, DataProperty) or isinstance(v, ObjectProperty) or isinstance(v, RdfTypeProperty):
                properties[k] = v
                print(k)
        for k, v in properties.items():
            attrs.pop(k)
        attrs['__properties__'] = properties 
        attrs['uri'] = PropertyUri("")
        attrs['__new_record__'] = True
        attrs['__destroyed__'] = False
        print(attrs)
        print(cls.__dict__)
        return type.__new__(cls, name, bases, attrs)

class Model(object, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        for name, value in kw.items():
            print(name)
            setattr(self, name, value)

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
            if key == "uri":
                return super().__setattr__(key, value)
            elif self.__properties__[key].has_one:
                self.__properties__[key].add(value)
            else:
                raise AttributeError(r"Cannot set attribute '%s' directly as it has cardinality of many. Use the add method" % key)
        except KeyError:
            raise AttributeError(r"A '%s' instance has no attribute named '%s'" % (self.__class__.__name__, key))

#    def save(self):
#        fields = []
#        params = []
#        args = []
#        for k, v in self.__properties__.items():
#            fields.append(v.name)
#            params.append('?')
#            args.append(getattr(self, k, None))
#        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#        print('SQL: %s' % sql)
#        print('ARGS: %s' % str(args))

    def properties(self):
        return self.__properties__

    def is_valid(self, operation):
        return True

    def _is_persisted(self):
        return not(self.__new_record__ or self.__destroyed__)

    def _what_operation(self):
        persisted = self._is_persisted()
        return ':update' if persisted else ':create'

    def _create_or_update(self, operation):

        print("CREATE or UPDATE")

        #endpoint = r"http://localhost:3030/test/query"
        #store = sparqlstore.SPARQLUpdateStore(autocommit=False)
        #store.open((endpoint,r"http://localhost:3030/test/update"))
    
        #Graph to add
        #default_graph = URIRef('http://example.org/default-graph')
        #ng = Graph(store, identifier=default_graph)
    
        other_graph = Graph(store='Memory')

        for kp, vp in self.__properties__.items():
            print("Property %s" % (vp.name))
            for kv, vv in vp.values_as_dict().items():
                print("Triple (%s,%s,%s)" % (self.uri, vp.predicate, vv.value))
                other_graph.add((self.uri, vp.predicate, vv.value))

        #ng += other_graph
        #ng.commit()

    def save(self):
        print("SAVE")
        operation = self._what_operation()
        print("Operation: ", operation)
        if not self.is_valid(operation): return self 
        self._create_or_update(operation)

    