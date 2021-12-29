from rdflib import Graph, Literal
from rdfogm.data_property import DataProperty
from rdfogm.object_property import ObjectProperty
from rdfogm.rdf_type_property import RdfTypeProperty
from rdfogm.property_uri import PropertyUri

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        properties = dict()
        for k, v in attrs.items():
            if isinstance(v, DataProperty) or isinstance(v, ObjectProperty) or isinstance(v, RdfTypeProperty):
                properties[k] = v
        for k, v in properties.items():
            attrs.pop(k)
        attrs['__properties__'] = properties 
        attrs['__uri__'] = PropertyUri("")
        attrs['__new_record__'] = True
        attrs['__destroyed__'] = False
        return type.__new__(cls, name, bases, attrs)

class Model(object, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        for name, value in kw.items():
            setattr(self, name, value)

    def __getattr__(self, key):
        try:
            self.__properties__[key].values
        except KeyError:
            raise AttributeError(r"A '%s' instance has no attribute named '%s'" % (key, self.__class__.__name__))

    def __setattr__(self, key, value):
        try:
            if self.__properties__[key].has_one:
                self.__properties__[key].add(value)
            else:
                raise AttributeError(r"Cannot set attribute '%s' directly as it has cardinality of many. Use the add method" % key)
        except KeyError:
            raise AttributeError(r"A '%s' instance has no attribute named '%s'" % (key, self.__class__.__name__))

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
            for kv, vv in vp.values.items():
                other_graph.add((self.__uri__, vp.predicate, vv.value))
                print("Adding %s" % (vv.value))

        #ng += other_graph
        #ng.commit()

    def save(self):
        print("SAVE")
        operation = self._what_operation()
        print("Operation: ", operation)
        if not self.is_valid(operation): return self 
        self._create_or_update(operation)

    