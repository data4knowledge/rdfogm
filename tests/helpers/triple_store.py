import requests
from requests.auth import HTTPBasicAuth

class TripleStore:
  
    def __init__(self):
        self.__cfg__ = self.__store_config()

    def clear(self, graph='DEFAULT'):
        if graph != 'DEFAULT':
            graph = f'GRAPH <{graph}>'
        self.__update(f'CLEAR {graph}')

    def upload(self, filename, graph=""):
        self.__upload(filename, graph)

    def query(self, sparql):
        self.__query(sparql)

    def update(self, sparql):
        self._update(sparql)

    def __query(self, sparql):
        headers = {'Accept': 'application/sparql-results+json', 'Content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(
            self.__endpoint('query'), 
            headers = headers,
            auth = self.__auth(),
            data = f'query={sparql}'
        )
        return response

    def __update(self, sparql):
        headers = {'Accept': 'application/sparql-results+json', 'Content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(
            self.__endpoint('update'), 
            headers = headers,
            auth = self.__auth(),
            data = f'update={sparql}'
        )
        return response

    def __upload(self, filename, graph=""):
        import os
        from requests_toolbelt import MultipartEncoder

        head, tail = os.path.split(filename)
        multipart_data = MultipartEncoder(fields={'file': (tail, open(filename, 'rb'), 'text/plain')}) 
        headers={'Content-Type': multipart_data.content_type}
        response=requests.put(self.__endpoint('data', graph), data=multipart_data, auth=self.__auth(),headers=headers)
        return response

    def __auth(self):
        return HTTPBasicAuth(self.__cfg__['username'], self.__cfg__['password'])
    
    def __endpoint(self, type, graph=""):
        protocol = self.__cfg__['protocol']
        host = self.__cfg__['host']
        port = self.__cfg__['port']
        ds = self.__cfg__['dataset']
        endpoint = f'{protocol}://{host}:{port}/{ds}/{type}'
        if graph != "":
            endpoint += f'?graph={graph}'
        return endpoint

    def __store_config(self):
        return {'protocol': 'http', 'host': 'localhost', 'port': '3030', 'dataset': 'test', 'username': '', 'password': ''}
