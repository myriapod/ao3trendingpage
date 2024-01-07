import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from packages.sqlconnect import SQLAlchemy

import csv

session = SQLAlchemy()
engine = session.engine()


workid_list = list(pd.read_sql("SELECT workid FROM stats", engine).to_dict()["workid"].values())

print(len(workid_list))

print(len(list(dict.fromkeys(workid_list))))
