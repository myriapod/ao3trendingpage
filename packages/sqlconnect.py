from sqlalchemy import create_engine
from dotenv import dotenv_values

class SQLAlchemy():
    def __init__(self):
        self.username = dotenv_values("packages/.env")["MDBUSER"]
        self.password = dotenv_values("packages/.env")["MDBPWD"]
        self.database = dotenv_values("packages/.env")["DATABASE"]
        self.table = dotenv_values("packages/.env")["TABLE"]
        self.host = dotenv_values("packages/.env")["SQLHOST"]

    def engine(self):
        return create_engine(f"mariadb+pymysql://{self.username}:{self.password}@{self.host}/{self.database}?charset=utf8mb4")