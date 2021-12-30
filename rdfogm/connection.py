from rdflib import Graph
from rdflib.plugins.stores import sparqlstore

class Connection(object):
    
    def __init__(self, graph):
        self.__query_endpoint = r"http://localhost:3030/test/query"
        self.__update_endpoint = r"http://localhost:3030/test/update"
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
        return self.__store.predicate_objects(subject)