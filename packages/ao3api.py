import AO3
from dotenv import dotenv_values
import time


class AO3API():
    def __init__(self):
        self.username = dotenv_values("packages/.env")["AO3USER"]
        self.password = dotenv_values("packages/.env")["AO3PWD"]
        self.waitingtime = 240
        
    def ao3_connect(self):
        ratelimit=True
        while ratelimit:
            try:
                session = AO3.Session(self.username, self.password)
                ratelimit=False
            except AO3.utils.HTTPError:
                print("session ratelimit")
                time.sleep(self.waitingtime)
        return session
    
    def ao3_work_search(self, workid, session=None):
        ratelimit=True
        while ratelimit:
            try:
                workdata = AO3.Work(workid=workid, session=session, load=True, load_chapters=False).metadata
                ratelimit = False
            except AO3.utils.HTTPError:
                print("session ratelimit")
                time.sleep(self.waitingtime)
        return workdata
