from packages.ao3tosql import AO3toSQL


fandom_list = []
with open(f'packages/fandom_list.txt', 'r') as fl:
    for line in fl.readlines():
        fandom_list.append(line)    

for fandom in fandom_list:
    search = AO3toSQL()
    search.ao3tosql_search(fandom=fandom)