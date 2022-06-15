import math
from configs.Elasticsearch.connection import es
from configs.config import getEnv
import json

es.client()

def getAllNews(search=None, size = None, page= None):
    
    try:
        pages = 1
        sizes = 10
        
        if size != None:
            sizes = size
            
        if page != None:
            pages = page
          
        esParams = {
            'from': (int(pages) - 1) * int(sizes),
            'size': int(sizes),
            'query':{
                'query': {
                    'bool': {
                        'must': []
                    }
                }
            }
        }
        
        if search == None:
            esParams['query'] = {
                'query': {
                    'match_all': {}
                }
            }
            
        if search:
            esParams['query']['query']['bool']['must'] = [
                {
                    'match': {
                        'judul': {
                            'query': search,
                            'operator': 'or'
                        }
                    }
                },
                {
                    'match': {
                        'konten': {
                            'query': search,
                            'operator': 'or'
                        }
                    }
                }
            ]
        
        
        resultSearch = es.search('news', esParams)
        resultCountData = es.countData('news', esParams)
       
        result = {
            'err': False, 
            'message':'Success get data!', 
            'data': resultSearch,
            'metaData': {
                'page': int(pages),
                'size': int(sizes),
                'totalData': int(resultCountData),
                'totalPages': math.ceil(int(resultCountData) / int(sizes))
            }
        }
        
        return result,200
    except Exception as e:
        print(e)
        result = {'err': True, 'message':'Internal Server Error', 'data': ''}
        code = 500
        return result,code
    
    
    
    
    