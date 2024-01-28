# Module Imports
import mariadb
import sys
import json
import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class SQLServer():
    def __init__(self):
        manual_env={
            "MDBUSER": os.environ.get('MDBUSER'),
            "MDBPWD": os.environ.get('MDBPWD'),
            "DATABASE": os.environ.get('DATABASE'),
            "TABLEDATA": os.environ.get('TABLEDATA'),
            "TABLEID": os.environ.get('TABLEID'),
            "TABLERANK": os.environ.get('TABLERANK'),
            "SQLHOST": os.environ.get('SQLHOST'),
            "AO3USER": os.environ.get('AO3USER'),
            "AO3PWD": os.environ.get('AO3PWD'),
            "AO3WAITINGTIME": os.environ.get('AO3WAITINGTIME')
            }
        self.username = manual_env["MDBUSER"]
        self.password = manual_env["MDBPWD"]
        self.host = manual_env["SQLHOST"]
        self.database = manual_env["DATABASE"]
        self.tabledata = manual_env["TABLEDATA"]
        self.tableid = manual_env["TABLEID"]
        self.tablerank = manual_env["TABLERANK"]
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
        self.cursor.execute(f"SELECT ranking FROM {self.tableid} WHERE workid={workid}")
        old_rank = [e[0] for e in self.cursor]

        if old_rank[0] == None : # new workid in the ranking table
            # self.cursor.execute(f"SElECT * FROM {self.tabledata} WHERE workid={workid} HAVING COUNT(*)=2") 
            self.cursor.execute(f'''INSERT INTO {self.tablerank} (workid, fandom, ranking, timestmp, keyword) VALUES ({workid}, "{fandom_name}", {rank}, "{timestamp}", "NEW")''')
            self.conn.commit()
            self.cursor.execute(f"UPDATE {self.tableid} SET ranking={rank}, keyword='NEW' WHERE workid={workid}")
            self.conn.commit()

        else:
            self.cursor.execute(f"SELECT * FROM {self.tablerank} WHERE workid={workid}")
            for e in self.cursor:
                rankDiff = int(old_rank[0] - rank)

                if rankDiff==0:
                    self.cursor.execute(f'''UPDATE {self.tablerank} SET ranking={rank}, keyword="=", timestmp="{timestamp}", fandom="{fandom_name}" WHERE workid={workid}''')
                    self.conn.commit()
                    self.cursor.execute(f'''UPDATE {self.tableid} SET ranking={rank}, keyword="=" WHERE workid={workid}''')
                    self.conn.commit()
                else:
                    self.cursor.execute(f"UPDATE {self.tableid} SET ranking={rank}, keyword={str(rankDiff)} WHERE workid={workid}")
                    self.conn.commit()
                    self.cursor.execute(f'''UPDATE {self.tablerank} SET ranking={rank}, keyword={str(rankDiff)}, timestmp="{timestamp}", fandom="{fandom_name}" WHERE workid={workid}''')
                    self.conn.commit()
                break
        # add an elif for the HOT label when it's not new but going strong
    
    def update_out_of_ranking(self, timestamp):
        self.cursor.execute(f"UPDATE {self.tablerank} SET ranking=NULL WHERE timestmp<>'{timestamp}'") # set the rank to 0 to the fics that have left the ranking

        self.conn.commit()

    def update_metadata(self, data):
        for entry in data:
            self.cursor.execute(f'''
                                UPDATE {self.tablerank} SET 
                                worktitle="{data[entry]["worktitle"]}",
                                authors="{data[entry]["authors"]}",
                                relationship="{data[entry]["relationship"]}",
                                chapters="{data[entry]["chapters"]}",
                                latest_updated="{data[entry]["latest_updated"]}",
                                categories="{data[entry]["categories"]}",
                                rating="{data[entry]["rating"]}",
                                tags="{data[entry]["tags"]}",
                                words={data[entry]["words"]}
                                WHERE workid={data[entry]["workid"]}
                                ''')
            self.conn.commit()

    def get_ranking_for_metadata(self):        
        data = {}
        self.cursor.execute(f"SELECT * FROM {self.tablerank} WHERE ranking IS NOT NULL ORDER BY ranking ASC")
        for rank in self.cursor:
            data[rank[2]] = {}
            data[rank[2]]["workid"] = rank[0]
        # print(data)
        return data

    def get_ranking_for_html(self):
        data = []
        self.cursor.execute(f"SHOW COLUMNS FROM {self.tablerank}")
        header = self.cursor.fetchall()

        self.cursor.execute(f"SELECT * FROM {self.tablerank} WHERE ranking IS NOT NULL ORDER BY ranking ASC")
        rows = self.cursor.fetchall()
        
        for t in rows:
            dic = {}
            for r in range(0, len(t)):
                dic[header[r][0]] = t[r]
            dic["link"] = f'https://archiveofourown.org/works/{dic["workid"]}'
            data.append(dic)

        return data

    def json_dump(self, jsfile: str): # not used
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