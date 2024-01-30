import AO3
import os
from dotenv import load_dotenv
from os.path import join, dirname
import time
from copy import deepcopy
from re import match
from sqlserver import SQLServer
import re

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class AO3toSQL():
    def __init__(self, timestamp):
        self.time = timestamp
        manual_env={
            "MDBUSER": os.environ.get('MDBUSER'),
            "MDBPWD": os.environ.get('MDBPWD'),
            "DATABASE": os.environ.get('DATABASE'),
            "TABLEDATA": os.environ.get('TABLEDATA'),
            "TABLEID": os.environ.get('TABLEID'),
            "TABLERANK": os.environ.get('TABLERANK'),
            "SQLHOST": os.environ.get('SQLHOST'),
            "AO3USER": os.environ.get('AO3USER'),
            "AO3PWD": os.environ.get('AO3PWD'),
            "AO3WAITINGTIME": os.environ.get('AO3WAITINGTIME')
            }
        self.username = manual_env["AO3USER"]
        self.password = manual_env["AO3PWD"]
        self.waitingtime = 240
        self.sqlserver = SQLServer()
        self.sqlserver.connection()
        # connect to the SQL server

        # connect to ao3
        ratelimit=True
        while ratelimit:
            try:
                self.session = AO3.Session(self.username, self.password)
                ratelimit=False
            except AO3.utils.HTTPError:
                print("session ratelimit")
                time.sleep(self.waitingtime)

    def ao3_workid_search(self, workid):
        # search a work with the workid - not used
        ratelimit=True
        while ratelimit:
            try:
                workdata = AO3.Work(workid=workid, session=self.session, load=True, load_chapters=False).metadata
                ratelimit = False
            except AO3.utils.HTTPError:
                print("session ratelimit")
                time.sleep(self.waitingtime)
        return workdata


    def ao3tosql_search(self, fandom, refandom, criteria=""):
        # search every fic for a fandom
        # fandom = keyword to search on ao3
        # refandom = regex form
        # criteria = apply a criteria on the search, like hits>100
        ratelimit=True
        while ratelimit:
            try:
                search = AO3.Search(fandoms=fandom, any_field=criteria) # add a small filter of only the fics with more than 100 hits to avoid the rate limits
                search.update()
                ratelimit=False
            except AO3.utils.HTTPError:
                print(f"search ratelimit - waiting {self.waitingtime}")
                time.sleep(self.waitingtime)

        fandom = fandom.strip().replace('*','')

        stats_format = {
                "fandom": fandom,
                "id": 0,
                "timestmp": self.time,
                "crossover": False,
                "comments": 0,
                "kudos": 0,
                "bookmarks": 0,
                "hits": 0,
                "date_edited": "1111-11-11",
                "date_published": "1111-11-11",
                "date_updated": "1111-11-11",
                } 

        iter = 0
        for i in range(1, search.pages+1):
            search.page=i
            ratelimit=True
            while ratelimit:
                try:
                    search.update()
                    ratelimit=False
                except AO3.utils.HTTPError:
                    printProgressBar(iteration=iter, total=search.total_results, prefix=f"data extraction for fandom {fandom}", suffix=f"hit rate limit - waiting {self.waitingtime} seconds")
                    time.sleep(self.waitingtime)

            for result in search.results: # type: ignore

                # need to check that the fandom name is really in the list of fandoms since there is no NO crossover options on the api
                if re.match(refandom, ' - '.join(result.metadata["fandoms"])):
                    iter += 1
                    # need to do a deep copy of the template for the dict because
                    statdata = deepcopy(stats_format)

                    # add a way to identify if a fic is crossover in the sql database
                    if len(result.metadata["fandoms"]) > 1:
                        statdata["crossover"] = True

                    for key in statdata.keys():
                        if key in result.metadata.keys():
                            if match("date*", key):
                                statdata[key] = str(result.metadata[key].split(" ")[0])
                            else:
                                statdata[key] = result.metadata[key]

                    self.sqlserver.add_data(statdata)
                    self.sqlserver.add_id(statdata)
                    print(f'{self.time} - Entered stats data for work {statdata["id"]}')
                    print("Progress = "+ "{:.2f}".format(100 * (iter / float(search.total_results))))

    def metadata_ranking(self):
        data = self.sqlserver.get_ranking_for_metadata()

        iter=0
        for entry in data:
            try:
                meta = self.ao3_workid_search(data[entry]["workid"])
                
                data[entry]["worktitle"] = meta["title"]
                data[entry]["authors"] = ' & '.join(meta["authors"])

                if meta["categories"]:
                    data[entry]["relationship"] = meta["relationships"][0]
                else: 
                    data[entry]["relationship"] = "N/A"

                if meta["expected_chapters"] == None:
                    data[entry]["chapters"] = f'{meta["nchapters"]}/?'
                else:
                    data[entry]["chapters"] = f'{meta["nchapters"]}/{meta["expected_chapters"]}'

                data[entry]["latest_updated"] = max(meta["date_updated"], meta["date_published"], meta["date_edited"]).split(" ")[0]

                if meta["categories"]:
                    if len(meta["categories"])>1:
                        data[entry]["categories"] = "Multi"
                    else:
                        data[entry]["categories"] = meta["categories"][0]
                else:
                    data[entry]["categories"] = "N/A"

                if meta["rating"]:
                    data[entry]["rating"] = meta["rating"]
                else:
                    data[entry]["rating"] = "N/A"
                
                if len(meta["tags"])>=4:
                    data[entry]["tags"] = ', '.join(meta["tags"][:4])
                else:
                    data[entry]["tags"] = ', '.join(meta["tags"])
                
                data[entry]["words"] = meta["words"]
                iter+=1
                print(f'{self.time} - Entered metadata for work {data[entry]["worktitle"]} ({data[entry]["workid"]})')
                print("Progress = "+ "{:.2f}".format(100 * (iter / float(len(data)))))
            except AttributeError as err:
                print(f'{self.time} - Error for {data[entry]["workid"]}')
                print(err)

        return data