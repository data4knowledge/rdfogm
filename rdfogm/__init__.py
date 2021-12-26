from rdflib import Graph, Literal
from rdfogm.data_property import DataProperty
from rdfogm.object_property import ObjectProperty

class ModelMetaclass(type):

    print("MMC")

    def __new__(cls, name, bases, attrs):
        print("MMC __new__ name", name)
        print("MMC __new__ bases", bases)
        print("MMC __new__ attrs", attrs)
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, DataProperty) or isinstance(v, ObjectProperty):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k, v in mappings.items():
            attrs.pop(k)
        attrs['__mappings__'] = mappings 
        attrs['__table__'] = name 
        return type.__new__(cls, name, bases, attrs)

class Model(object, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        for name, value in kw.items():
            setattr(self, name, value)

    def __getattr__(self, key):
        try:
            super().__getattr__(key)
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
