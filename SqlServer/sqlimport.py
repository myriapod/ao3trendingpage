# Module Imports
import mariadb
import sys
from dotenv import dotenv_values

class SQLServer():
    def __init__(self):
        self.username = dotenv_values(".env")["MDBUSER"]
        self.password = dotenv_values(".env")["MDBPWD"]
        self.host="localhost"
        self.database="ao3trendingpage"
        self.table="stats"
        self.cursor = None
        self.conn = None

    def connection(self):
        # Connect to MariaDB Platform
        try:
            self.conn = mariadb.connect(
                user=self.username,
                password=self.password,
                host=self.host,
                database=self.database
            )

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Get Cursor
        self.cursor = self.conn.cursor()

    def add(self, data):
        for entry in data:
            self.cursor.execute(
                f'''INSERT INTO {self.table} 
                (fandom, workid, timestmp, comments, kudos, bookmarks, hits, date_edited, date_published, date_updated) 
                VALUES 
                {entry["fandom"], entry["id"], entry["timestmp"], entry["comments"], entry["kudos"], entry["bookmarks"], entry["hits"], entry["date_edited"], entry["date_published"], entry["date_updated"]}'''
                )
            print(f'added {entry["fandom"]}, {entry["id"]}')
        
            self.conn.commit()
            
    def remove(self, data): # to do
        for entry in data:
            self.cursor.execute(
                f'REMOVE FROM {self.table} '
                )

    def disconnection(self):
        self.cursor.close()
        self.conn.close()