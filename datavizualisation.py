from packages.ao3tosql import AO3toSQL
from pprint import pp
import sys

def main(timestamp):
    ao3 = AO3toSQL(timestamp=timestamp)
    metadata = ao3.metadata_ranking()
    ao3.sqlserver.update_metadata(metadata)

if __name__ == "__main__":
    timestamp = ' '.join([sys.argv[1], sys.argv[2]])
    main(timestamp=timestamp)