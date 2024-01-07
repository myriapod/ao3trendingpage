import AO3
from dotenv import dotenv_values
from datetime import datetime
from copy import deepcopy
from re import match


class Search():
    def __init__(self):
        self.statdata={}
        self.username = dotenv_values(".env")["USERNAME"]
        self.password = dotenv_values(".env")["PASSWORD"]
        self.results = []
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def ao3_connect(self):
        return AO3.Session(self.username, self.password)

    def ao3_search(self, fandom):
        search = AO3.Search(fandoms=fandom)
        search.update()
        fandom = fandom.strip().replace('*','')
        # will be removed, just for monitoring during dev phase
        print(fandom, search.total_results, search.pages,len(search.results)) # type: ignore

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

        
        
        for i in range(0, search.pages):
            search.page=i
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
                self.results.append(statdata)
        return self.results