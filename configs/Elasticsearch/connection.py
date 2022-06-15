from elasticsearch import Elasticsearch
from ..config import getEnv

import json

class ElasticsearchDb:
    
    def __init__(self):
        self.conn = None

    def client(self):
        self.conn = Elasticsearch(getEnv('ELASTICSEARCH_HOST'))
    
    def clientInfo(self):
        res = self.conn.info()
        return res
    
    def search(self, indexName, body):
        res = self.conn.search(index=indexName,body=body['query'], size=body['size'], from_=body['from'])
        hits = res['hits']['hits']
        newData = []
        
        for item in hits:
            newData.append(item['_source'])
        
        return newData
    
    def countData(self, indexName, body):
        res = self.conn.count(index=indexName, body=body['query'])
        return res['count']

es = ElasticsearchDb()