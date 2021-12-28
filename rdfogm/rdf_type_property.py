from rdfogm.base_property import BaseProperty
from rdflib import RDF

class RdfTypeProperty(BaseProperty):

    def __init__(self, rdf_type):
        super().__init__(**{'name': "rdf_type", 'predicate': RDF.type})
        self.add(rdf_type)
