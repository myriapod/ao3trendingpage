from packages.ao3tosql import AO3toSQL
import csv


search = AO3toSQL()
with open(f'packages/fandom_list.csv', 'r') as fl:
    csvfile = csv.DictReader(fl)
    for row in csvfile:
        search.ao3tosql_search(fandom=row["fandom"], refandom=row["refandom"])