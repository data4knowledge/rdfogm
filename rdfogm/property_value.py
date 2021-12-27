class PropertyValue(object):

    def __init__(self, value=None):
        self.__value = value
        self.__modified = False
        if value != None:
            self.__modified = True

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

    def __str__(self):
        return self.__value.__str__()
    