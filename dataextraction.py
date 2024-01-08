from packages.ao3search import AO3toSQL
from packages.sqlimport import SQLServer


fandom_list = []
with open(f'packages/fandom_list.txt', 'r') as fl:
    for line in fl.readlines():
        fandom_list.append(line)    

for fandom in fandom_list:
    search = AO3toSQL()
    search.ao3_connect()
    search.ao3tosql_search(fandom=fandom) # a list of dicts