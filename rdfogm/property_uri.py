import base64

from rdflib.term import URIRef

class PropertyUri(URIRef):
    
    def __init__(self, value):
        self.__uri = URIRef(value)

    def to_id(self):
        message_bytes = self.__uri.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        return base64_bytes.decode('ascii')

    @classmethod
    def from_id(cls, id):
        base64_bytes = id.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        return PropertyUri(message_bytes.decode('ascii'))

    def __str__(self):
        return self.__uri.__str__()




message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')