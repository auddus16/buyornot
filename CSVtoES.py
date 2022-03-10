import json
import urllib
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers
from urllib.request import Request, urlopen

import csv

es = Elasticsearch(['3.34.219.4:9200'])
docs = []
j = 0

with open('API가져오기/seoul_500to1000.csv', 'r', encoding='UTF8') as se:
    reader = csv.reader(se)
    lee = 0
    for i in reader:
        lee+=1
        if (lee == 1000):
            break
        if(i==0):
            continue
        ht = i[16]


        hf = hf.split('/')
        length=0;
        dataName =''
        dataType =''
        for j in hf:
            if(length==4):
                dataType = j
            if(length==5):
                dataName =j
            length+=1

        #hf[4]  = type (xml,json)
        #hf[5] = dataName
        #hf[6] = start
        #hf[7] = end
        link =''
        for j in hf:
            if(j=='(인증키)'):
                link+='474a76586572727733385465625659'+'/'
            else:
                link +=j+'/'
        if(dataType=='xml'):
            for j in range(0, 100000):
                iStart = (j) * 1000 + 1
                iEnd = (j + 1) * 1000
                link = ''
                cnt = 0;
                for k in hf:
                    if (cnt == 3):
                        link += '474a76586572727733385465625659'+ '/'
                    elif (cnt == 6):
                        link += str(iStart) + '/'
                    elif (cnt == 7):
                        link += str(iEnd) + '/'
                    else:
                        link += k + '/'
                    cnt += 1
                print(link);
                response = urllib.request.urlopen(link)
                xml_str = response.read().decode('utf-8')
                tree = ElementTree(fromstring(xml_str))
                root = tree.getroot()
                index =root.tag
                print(index)
                for res in root.iter("RESULT"):
                    mesg = res[1].text
                if(mesg !='정상 처리되었습니다'):
                    break
                id = iStart
                for row in root.iter("row"):
                    dic ={}
                    for column in row:
                        dic[column.tag] = column.text
                    doc = {
                        "_index":"lee",
                        "_id":id,
                        "_source":dic
                    }
                    docs.append(doc)
                    id+=1
        elif(dataType=='json'):
            for j in range(0, 100000):
                iStart = (j) * 1000 + 1
                iEnd = (j + 1) * 1000
                link = ''
                cnt = 0;
                for k in hf:
                    if (cnt == 3):
                        link += '474a76586572727733385465625659'+ '/'
                    elif (cnt == 6):
                        link += str(iStart) + '/'
                    elif (cnt == 7):
                        link += str(iEnd) + '/'
                    else:
                        link += k + '/'
                    cnt += 1
                print(link);
                response = urllib.request.urlopen(link)
                api = response.read().decode("utf-8")
                jsos = json.loads(api)
                string = jsos.keys()
                dic = {}
                for i in string:
                    fileName = i
                if (jsos[fileName]['RESULT']['MESSAGE'] != '정상 처리되었습니다.'):
                    break
                string = jsos[fileName]['row']
                for i in string:
                    keys = i.items()
                    for j in keys:
                        dic[j[0]] = j[1]
                id =iStart
                doc = {
                    "_index": "lee",
                    "_id": id,
                    "_source": dic
                }
                id+=1
                docs.append(doc)
        helpers.bulk(es, docs)





