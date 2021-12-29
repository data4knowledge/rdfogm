from rdflib.term import URIRef

class PropertyUri(URIRef):
    
    def __init__(self, value):
        self.__uri = URIRef(value)

    def __str__(self):
        return self.__uri.__str__()
