from rdflib import Literal

class PropertyLiteral(Literal):
    
    def __init__(self, value, language=None):
        self.__literal = Literal(value, lang=language)

    def key(self):
        return f"{self.__literal.__str__()}.{self.__literal.language}"

    def __str__(self):
        return self.__literal.__str__()
