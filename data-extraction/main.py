import AO3
from dotenv import dotenv_values
from datetime import datetime
import csv


ao3session = dotenv_values(".env")
username = ao3session["USERNAME"]
password = ao3session["PASSWORD"]

session = AO3.Session(username, password)

file_storage = ""

fandom_list = []
with open(f'{file_storage}/fandom_list.txt', 'r') as fl:
    for line in fl.readlines():
        fandom_list.append(line)


for fandom in fandom_list:
    search = AO3.Search(fandoms=fandom)
    timestamp = datetime.now()
    search.update()
    fandom = fandom.strip().replace('*','')
    print(fandom, search.total_results, search.pages,len(search.results)) # type: ignore
    for i in range(0,search.pages):
        search.page=i
        for result in search.results: # type: ignore
            workdata = result.metadata
            workdata["timestamp"] = timestamp
        
            with open(f'{file_storage}/{fandom}/{fandom}_{timestamp}.csv', 'a') as f:
                w = csv.DictWriter(f, workdata.keys())
                w.writerow(workdata)

# metadata
''' normal_fields = (
            "bookmarks", 
            "categories",
            "nchapters",
            "characters",
            "complete",
            "comments",
            "expected_chapters",
            "fandoms",
            "hits",
            "kudos",
            "language",
            "rating",
            "relationships",
            "restricted",
            "status",
            "summary",
            "tags",
            "title",
            "warnings",
            "id",
            "words",
            "collections"
        )
        string_fields = (
            "date_edited",
            "date_published",
            "date_updated",
        )
        timestamp'''

