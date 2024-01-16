# Module Imports
import mariadb
import sys
from dotenv import dotenv_values

class SQLServer():
    def __init__(self):
        self.username = dotenv_values("packages/.env")["MDBUSER"]
        self.password = dotenv_values("packages/.env")["MDBPWD"]
        self.host = dotenv_values("packages/.env")["SQLHOST"]
        self.database = dotenv_values("packages/.env")["DATABASE"]
        self.tabledata = dotenv_values("packages/.env")["TABLEDATA"]
        self.tableid = dotenv_values("packages/.env")["TABLEID"]
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

    def add_data(self, entry):
        self.cursor.execute(f'''
                            INSERT INTO {self.tabledata} 
                            (fandom, workid, timestmp, crossover, comments, kudos, bookmarks, hits, date_edited, date_published, date_updated) 
                            VALUES 
                            {entry["fandom"], entry["id"], entry["timestmp"], entry["crossover"], entry["comments"], entry["kudos"], entry["bookmarks"], entry["hits"], entry["date_edited"], entry["date_published"], entry["date_updated"]}
                            ''')
        # print(f'added {entry["fandom"]}, {entry["id"]}')
    
        self.conn.commit()
            
    def add_id(self, entry):
        self.cursor.execute(f'''
                            INSERT INTO {self.tableid} (workid)
                            SELECT {entry["id"]}
                            WHERE NOT EXISTS
                                (SELECT 1
                                FROM {self.tableid}
                                WHERE workid={entry["id"]})
                            ''')
        self.conn.commit()

    def get_last_two(self, workid):
        last_two = []
        self.cursor.execute(f"SELECT * FROM {self.tabledata} WHERE workid={workid} ORDER BY id DESC LIMIT 2")
        for entry in self.cursor:
            last_two.append(entry)
        return last_two
        
    def get_list_workid(self):
        list_workid = []
        self.cursor.execute(f"SELECT workid FROM {self.tableid}")
        for (workid, ) in self.cursor:
            list_workid.append(workid)
        return list_workid

    def update_stats(self, workid, commentsDiff, kudosDiff, bookmarksDiff, hitsDiff):
        self.cursor.execute(f"UPDATE {self.tableid} SET commentsDiff = {commentsDiff}, kudosDiff = {kudosDiff}, bookmarksDiff = {bookmarksDiff}, hitsDiff = {hitsDiff} WHERE workid={workid}")
        self.conn.commit()

    def get_top_10(self, crossover=False):
        top_ten = []
        
        if crossover:
            self.cursor.execute(f"SELECT * FROM {self.tableid} ORDER BY hitsDiff DESC LIMIT 10")
        else:
            self.cursor.execute(f"SELECT {self.tableid}.* from {self.tableid} order by hitsDiff DESC LIMIT 10 WHERE {self.tableid}.workid in (SELECT {self.tabledata}.workid from {self.tabledata} WHERE {self.tabledata}.crossover=false)")
            
        for top in self.cursor:
            top_ten.append(top)
        return top_ten

    def disconnection(self):
        self.cursor.close()
        self.conn.close()