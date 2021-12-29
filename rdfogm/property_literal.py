from rdflib import Literal

class PropertyLiteral(Literal):
    
    def __init__(self, value, lang=None):
        self.__literal = Literal(value, lang=lang)

    def __str__(self):
        return self.__literal.__str__()
