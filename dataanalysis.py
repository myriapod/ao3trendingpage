import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from packages.sqlconnect import SQLAlchemy

import csv

session = SQLAlchemy()
engine = session.engine()


workid_list = list(pd.read_sql(f"SELECT workid FROM {session.tableid}", engine).to_dict()["workid"].values())

for workid in workid_list:
    dict_res = pd.read_sql(f"SELECT * FROM {session.tabledata} WHERE workid={workid} ORDER BY id DESC LIMIT 2", engine).to_dict()
    
    commentsDiff = dict_res["1"]["comments"]-dict_res["2"]["comments"]
    kudosDiff = dict_res["1"]["kudos"]-dict_res["2"]["kudos"]
    bookmarksDif = dict_res["1"]["bookmarks"]-dict_res["2"]["bookmarks"]
    commentsDiff = dict_res["1"]["comments"]-dict_res["2"]["comments"]
    hitsDiff = dict_res["1"]["hits"]-dict_res["2"]["hits"]

    insert_id = pd.read_sql(f"INSERT (commentsDiff, kudosDiff, bookmarksDiff, commentsDiff, hitsDiff) INTO {self.tableid} VALUES commentsDiff, kudosDiff, bookmarksDiff, commentsDiff, hitsDiff WHERE workid={workid}", engine)