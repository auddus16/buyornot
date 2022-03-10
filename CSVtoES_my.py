import json
import urllib
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers
from urllib.request import Request, urlopen
import csv

es = Elasticsearch(['https://buyornot.kb.ap-northeast-2.aws.elastic-cloud.com:9243'])

docs = []
j = 0

if es.indices.exists(index='my-index'):
    pass
else:
    es.indices.create(index='my-index')
with open('당근마켓_t2.csv', 'r', encoding='UTF8') as se:
    reader = csv.DictReader(se)
    helpers.bulk(es, reader, index='my-index', doc_type='my-type')



