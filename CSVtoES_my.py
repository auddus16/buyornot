# -*- coding: utf-8 -*-
import datetime
import json
import urllib
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers
from urllib.request import Request, urlopen
import csv
import pandas as pd

es = Elasticsearch(['https://buyornot.kb.ap-northeast-2.aws.elastic-cloud.com:9243'], http_auth=('elastic', 'Orf5PC90BVmMMuVU5cKoTyrs'))
es.indices.create(
    index='python_to_elastic',
    body={
        "mappings" : {
            "type1" : {
                "properties" : {
                    "field1" : {
                        "type" : "text"
                      }
                  }
              }
          }
      }
  )
es.create(
    index='python_to_elastic',
    doc_type='type1',
    body= {
        "doc" : {
            "field1" : "value2"
         }
     },
     id = 'abc111'
)

docs = []
j = 0

# if es.indices.exists(index='daangn-index'):
#     pass
# else:
#     es.indices.create(index='daangn_index')
# file= pd.read_excel('당근마켓_220316_1200.xlsx')
# file.to_csv('당근마켓_220316_1200.csv', index=False)

# with open('당근마켓_220316_1200.csv', 'r', encoding='UTF8', errors='ignore') as se:
#     reader = csv.reader(se)
#     doc = {
#         "_index": "carrot_market",
#         "_type" : "aaa",
#         "_id" : "aaa",
#         "_source": {
#             "datalink" : "당근마켓",
#             "name" : "애플"
#         }
#     }
#     docs.append(doc)
#     helpers.bulk(es, docs)




