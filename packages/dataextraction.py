from ao3tosql import AO3toSQL
import csv
import sys

def main(timestamp):
    search = AO3toSQL(timestamp=timestamp)
    search.ao3_connect()

    with open(f'packages/fandom_list.csv', 'r') as fl:
        csvfile = csv.DictReader(fl)

        for row in csvfile:
            search.ao3tosql_search(fandom=row["fandom"], refandom=row["refandom"], criteria="hits>100")

if __name__ == "__main__":
    timestamp = ' '.join([sys.argv[1], sys.argv[2]])
    main(timestamp=timestamp)