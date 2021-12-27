from rdflib.namespace import XSD

class PropertyValue(object):

    def __init__(self):
        self.__modified = False
        self.__value = None

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
        self.__modified = True

    def to_be_saved(self):
        return self.__modified
       
    def saved(self):
       self.__modified = False 