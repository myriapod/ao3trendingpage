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

work = AO3.Work(workid=id)

workdata = deepcopy(data_format)

for key in work.metadata.keys():
    if key in workdata.keys():
        workdata[key] = work.metadata[key]