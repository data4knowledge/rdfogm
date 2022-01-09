from rdflib import Graph
from rdflib.plugins.stores import sparqlstore
from rdfogm.settings import Settings

class Connection(object):
    
    def __init__(self, graph):
        self.__query_endpoint = self.__endpoint('query')
        self.__update_endpoint = self.__endpoint('update')
        self.__store = sparqlstore.SPARQLUpdateStore(autocommit=False)
        self.__store.open((self.__query_endpoint,self.__update_endpoint))
        self.__default_graph_uri = graph
        self.__default_graph = Graph(self.__store, identifier=self.__default_graph_uri)

    def default_graph(self):
        return self.__default_graph

    def temporary_graph(self):
        self.__temp_graph = Graph(store='Memory')
        return self.__temp_graph

    def add(self, subject, predicate, object):
        self.__temp_graph.add((subject, predicate, object))

    def commit(self):
        self.__default_graph += self.__temp_graph
        self.__default_graph.commit()
        self.__temp_graph = None

    def find(self, subject):
        return self.__default_graph.predicate_objects(subject)

    def __endpoint(self, type):
        settings = Settings()
        protocol = settings.protocol
        host = settings.host
        port = settings.port
        ds = settings.dataset
        return f'{protocol}://{host}:{port}/{ds}/{type}'
