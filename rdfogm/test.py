#from rdfogm.data_property import DataProperty
#from rdflib import Graph, Literal

print("RDFOGM 1:")

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

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
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k, v in mappings.items():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(object, metaclass=ModelMetaclass):
    #__metaclass__ = ModelMetaclass

    print("M")

    def __init__(self, **kw):
        print("M __init__", kw)
        #self.id = kw["id"]
        for name, value in kw.items():
            setattr(self, name, value)
        #Model.__init__(self)

    def __getattr__(self, key):
        print("M __getattr__")
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

#    def __setattr__(self, key, value):
#        print("M __setattr__", key, value)
##        setattr(self, key, value)
#        #self.__mappings__[key] = value

    def save(self):
        print("M save")
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

# testing code:

print("RDFOGM 2: ")

class User(Model):
    id = IntegerField('uid')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

print("RDFOGM 3: ", User)

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

print("RDFOGM 4: ", u.__dict__, u.email, u.__mappings__)

