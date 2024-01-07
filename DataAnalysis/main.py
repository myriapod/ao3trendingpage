import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import dotenv_values


username = dotenv_values(".env")["MDBUSER"]
password = dotenv_values(".env")["MDBPWD"]

engine = create_engine(f"mariad:///?User={username}&;Password={password}&Database=ao3trendingpage&Server=localhost")
