import AO3
from dotenv import dotenv_values
from datetime import datetime
import csv
from pprint import pprint
from copy import deepcopy

ao3session = dotenv_values(".env")
username = ao3session["USERNAME"]
password = ao3session["PASSWORD"]

session = AO3.Session(username, password)

file_storage = ""

fandom_list = []
with open(f'{file_storage}fandom_list.txt', 'r') as fl:
    for line in fl.readlines():
        fandom_list.append(line)

data_format = {"authors": "",
                "categories": "",
                "characters": "",
                "complete": "",
                "expected_chapters": "",
                "fandoms": "",
                "language": "",
                "nchapters": "",
                "rating": "",
                "relationships": "",
                "restricted": "",
                "series": "",
                "status": "",
                "summary": "",
                "tags": "",
                "title": "",
                "warnings": "",
                "words": "",
                "id": "",
                }
stats_format = {"id": "",
                "timestamp": "",
                "comments": "",
                "kudos": "",
                "bookmarks": "",
                "hits": "",
                "date_edited": "",
                "date_published": "",
                "date_updated": "",
                }       

for fandom in fandom_list:
    search = AO3.Search(fandoms=fandom)
    timestamp = datetime.now()
    search.update()

    fandom = fandom.strip().replace('*','')
    print(fandom, search.total_results, search.pages,len(search.results)) # type: ignore

    with open(f'{file_storage}{fandom}/{fandom}_{timestamp}_metadata.csv', 'w') as f:
        w = csv.DictWriter(f, data_format.keys())
        w.writeheader()
    with open(f'{file_storage}{fandom}/{fandom}_{timestamp}.csv', 'w') as f:
        w = csv.DictWriter(f, stats_format.keys())
        w.writeheader()
    
    for i in range(0,search.pages):
        search.page=i
        for result in search.results: # type: ignore
            workdata = deepcopy(data_format)
            statdata = deepcopy(stats_format)
            statdata["timestamp"] = timestamp # type: ignore
            
            for key in result.metadata.keys():
                if key in workdata.keys():
                    workdata[key] = result.metadata[key]
                if key in statdata.keys():
                    statdata[key] = result.metadata[key]

            with open(f'{file_storage}{fandom}/{fandom}_{timestamp}_metadata.csv', 'a') as f:
                w = csv.DictWriter(f, workdata.keys())
                w.writerow(workdata)
            with open(f'{file_storage}{fandom}/{fandom}_{timestamp}.csv', 'a') as f:
                w = csv.DictWriter(f, stats_format.keys())
                w.writerow(statdata)