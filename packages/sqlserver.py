# Module Imports
import mariadb
import sys
from dotenv import dotenv_values
import json

class SQLServer():
    def __init__(self):
        self.username = dotenv_values("packages/.env")["MDBUSER"]
        self.password = dotenv_values("packages/.env")["MDBPWD"]
        self.host = dotenv_values("packages/.env")["SQLHOST"]
        self.database = dotenv_values("packages/.env")["DATABASE"]
        self.tabledata = dotenv_values("packages/.env")["TABLEDATA"]
        self.tableid = dotenv_values("packages/.env")["TABLEID"]
        self.tablerank = dotenv_values("packages/.env")["TABLERANK"]
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
            
    def add_id(self, entry): # rework
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
            self.cursor.execute(f"SELECT {self.tableid}.* FROM {self.tableid} WHERE ({self.tableid}.workid) IN (SELECT {self.tabledata}.workid FROM {self.tabledata} WHERE {self.tabledata}.crossover=false) ORDER BY hitsDiff DESC LIMIT 10")
            
        for top in self.cursor:
            top_ten.append(top)
        return top_ten
    
    def update_ranking(self, workid, fandom_name, rank, timestamp):
        # if the work is already in the ranking
        self.cursor.execute(f"SELECT * FROM {self.tablerank} WHERE workid={workid}")
        if len(self.cursor.fetchall())!=0:
            self.cursor.execute(f"SELECT * FROM {self.tablerank} WHERE workid={workid}")
            for e in self.cursor:
                rankDiff = str(e[2] - rank)
                self.cursor.execute(f'''UPDATE {self.tablerank} SET ranking={rank}, keyword={rankDiff}, timestmp="{timestamp}", fandom="{fandom_name}" WHERE workid={workid}''')
                self.conn.commit()
                self.cursor.execute(f"UPDATE {self.tableid} SET ranking={rank}, keyword={rankDiff} WHERE workid={workid}")
                self.conn.commit()
                break
        # add an elif for the HOT label when it's not new but going strong
        else: # new workid in the ranking table
            # self.cursor.execute(f"SElECT * FROM {self.tabledata} WHERE workid={workid} HAVING COUNT(*)=2") 
            print("no work: ")
            self.cursor.execute(f"UPDATE {self.tablerank} SET ranking=NULL WHERE timestmp<>'{timestamp}'") # set the rank to 0 to the fics that have left the ranking
            self.conn.commit()
            self.cursor.execute(f'''INSERT INTO {self.tablerank} (workid, fandom, ranking, timestmp, keyword) VALUES ({workid}, "{fandom_name}", {rank}, "{timestamp}", "NEW")''')
            self.conn.commit()
            self.cursor.execute(f"UPDATE {self.tableid} SET ranking={rank}, keyword='NEW' WHERE workid={workid}")
            self.conn.commit()
        self.conn.commit()

    def json_dump(self, jsfile: str):
        keys=[]
        self.cursor.execute(f"SHOW COLUMNS FROM {self.tablerank}")
        for e in self.cursor:
            keys.append(e[0])

        self.cursor.execute(f"SELECT * FROM {self.tablerank} WHERE ranking IS NOT NULL")
        for entry in self.cursor:
            data = {}
            for index in range(0,len(entry)-1):
                data[keys[index]] = entry[index]
            with open(jsfile, 'a') as fl:
                json.dump(data, fl, indent=4, default=str)
                fl.write(", \n") #formatting



    def disconnection(self):
        self.cursor.close()
        self.conn.close()