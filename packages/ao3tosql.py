import AO3
from dotenv import dotenv_values
from datetime import datetime
import time
from copy import deepcopy
from re import match
from .sqlimport import SQLServer
from .ao3api import AO3API


class AO3toSQL():
    def __init__(self):
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.waitingtime = 240
        self.sqlserver = SQLServer()
        self.sqlserver.connection()
        AO3session = AO3API()
        self.ao3session = AO3session.ao3_connect()

    def ao3tosql_search(self, fandom):
        ratelimit=True
        while ratelimit:
            try:
                search = AO3.Search(fandoms=fandom, any_field="hits>100, crossovers=F") # add a small filter of only the fics with more than 100 hits to avoid the rate limits
                search.update()
                ratelimit=False
            except AO3.utils.HTTPError:
                print(f"search ratelimit - waiting {self.waitingtime}")
                time.sleep(self.waitingtime)

        fandom = fandom.strip().replace('*','')
        # will be removed, just for monitoring during dev phase
        print(fandom, search.total_results) # type: ignore

        stats_format = {
                "fandom": fandom,
                "id": 0,
                "timestmp": self.time,
                "comments": 0,
                "kudos": 0,
                "bookmarks": 0,
                "hits": 0,
                "date_edited": "1111-11-11",
                "date_published": "1111-11-11",
                "date_updated": "1111-11-11",
                } 

        
        for i in range(1, search.pages+1):
            search.page=i
            ratelimit=True
            while ratelimit:
                try:
                    search.update()
                    ratelimit=False
                except AO3.utils.HTTPError:
                    print(f"update ratelimit - waiting {self.waitingtime}")
                    time.sleep(self.waitingtime)

            for result in search.results: # type: ignore
                # need to do a deep copy of the template for the dict because
                # it's possible that not all the keys are in the result keys
                # for ex: if 0 comments then the key doesn't appear in result
                statdata = deepcopy(stats_format)
                for key in statdata.keys():
                    if key in result.metadata.keys():
                        if match("date*", key):
                            statdata[key] = str(result.metadata[key].split(" ")[0])
                        else:
                            statdata[key] = result.metadata[key]

                self.sqlserver.add_data(statdata)
                self.sqlserver.add_id(statdata)
                print(f'added {fandom} - {statdata["id"]}')