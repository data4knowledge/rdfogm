from rdfogm import Model, ObjectProperty, DataProperty, RdfTypeProperty, PropertyUri

class TestPerson(Model):
    rdf_type = RdfTypeProperty(PropertyUri("http://www.w3.org/TypeX"))
    name = DataProperty(**{'name': 'name', 'cardinality': 'one', 'predicate': PropertyUri("http://www.w3.org/name")})
    surname = DataProperty(**{'name': 'surname', 'cardinality': 'one', 'predicate': PropertyUri("http://www.w3.org/surname")})
    has_default = DataProperty(**{'name': 'has_default', 'cardinality': 'one', 'default': 'xxx', 'predicate': PropertyUri("http://www.w3.org/default")})
    nicknames = DataProperty(**{'name': 'nicknames', 'cardinality': 'many', 'predicate': PropertyUri("http://www.w3.org/nickname")})
    rel = ObjectProperty(**{'name': 'rel', 'predicate': PropertyUri("http://www.w3.org/rel")})
    links = ObjectProperty(**{'name': 'links', 'cardinality': 'many', 'predicate': PropertyUri("http://www.w3.org/links")})

    def __init__(self):
        super().__init__()

instance = TestPerson()
s = vars(TestPerson())
print(s)