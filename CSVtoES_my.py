import json
import urllib
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers
from urllib.request import Request, urlopen
import csv
import pandas as pd

es = Elasticsearch(['https://buyornot.kb.ap-northeast-2.aws.elastic-cloud.com:9243'])

docs = []
j = 0

# if es.indices.exists(index='daangn-index'):
#     pass
# else:
#     es.indices.create(index='daangn_index')
file= pd.read_excel('당근마켓_t3.xlsx')
file.to_csv('당근마켓_log1.csv')

with open('당근마켓_log1.csv', 'rt', encoding='UTF8', errors='ignore') as se:
    reader = csv.reader(se)
    helpers.bulk(es, reader, index='daangn-index')



