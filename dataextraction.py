from packages.ao3search import Search
from packages.sqlimport import SQLServer


fandom_list = []
with open(f'packages/fandom_list.txt', 'r') as fl:
    for line in fl.readlines():
        fandom_list.append(line)    

for fandom in fandom_list:
    search = Search()
    search.ao3_connect()
    results = search.ao3_search(fandom=fandom) # a list of dicts

    sqlserver = SQLServer()
    sqlserver.connection()
    sqlserver.add(results)
    sqlserver.disconnection()