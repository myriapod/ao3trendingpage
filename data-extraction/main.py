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
                "stats": {"timestamp": "",
                        "comments": "",
                        "kudos": "",
                        "bookmarks": "",
                        "hits": "",
                        "date_edited": "",
                        "date_published": "",
                        "date_updated": ""
                        },
                "status": "",
                "summary": "",
                "tags": "",
                "title": "",
                "warnings": "",
                "words": "",
                "id": "",
                }

for fandom in fandom_list:
    search = AO3.Search(fandoms=fandom)
    timestamp = datetime.now()
    search.update()
    fandom = fandom.strip().replace('*','')
    print(fandom, search.total_results, search.pages,len(search.results)) # type: ignore
    for i in range(0,search.pages):
        search.page=i
        for result in search.results: # type: ignore
            workdata = deepcopy(data_format)
            for key in workdata.keys():
                if key in result.metadata.keys():
                    workdata[key] = result.metadata[key]
                elif key == "stats":
                    for keyk in workdata["stats"]:
                        if keyk in result.metadata.keys():
                            workdata["stats"][keyk] = result.metadata[keyk]
            workdata["stats"]["timestamp"]=timestamp

            with open(f'{file_storage}{fandom}/{fandom}_{timestamp}.csv', 'a') as f:
                w = csv.DictWriter(f, workdata.keys())
                w.writerow(workdata)