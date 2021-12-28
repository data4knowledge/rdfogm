from rdflib import Graph, Literal
from rdfogm.data_property import DataProperty
from rdfogm.object_property import ObjectProperty
from rdfogm.property_uri import PropertyUri

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        properties = dict()
        for k, v in attrs.items():
            if isinstance(v, DataProperty) or isinstance(v, ObjectProperty):
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

#    def __getattr__(self, key):
#        try:
#            super().__getattr__(key)
#        except KeyError:
#            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

#    def __setattr__(self, key, value):
#        super().__setattr__(key, value)

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

    def _create_or_update(operation):
        pass
#        sparql = Sparql::Update.new(@transaction)
#        sparql.default_namespace(@uri.namespace)
#        to_sparql(sparql, recurse)
#        operation == :create ? sparql.create : sparql.update(@uri)

#        sparql.add({uri: @uri}, {prefix: :rdf, fragment: "type"}, {uri: self.class.rdf_type})
#        self.properties.each do |property|
#            next if object_empty?(property)
#            property.to_triples(sparql, @uri)
#            serialize_object(sparql, property, ignore_persistence) if recurse
#        end

    def save(self):
        operation = self._what_operation()
        if not self.is_valid(operation): return self 
        self._create_or_update(operation)

    