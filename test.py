from packages.sqlserver import SQLServer
from pprint import pp
import json
import sys


server = SQLServer()
server.connection()

def main(timestamp):
    print(timestamp)


top_ten = [(24620431, None, 8, 39, 1, 1613, None),
 (50941855, None, 17, 32, 1, 781, None),
 (47507560, None, 16, 26, 6, 742, None),
 (20176075, None, 1, 19, 1, 668, None),
 (27002017, None, 17, 28, 5, 588, None),
 (44044893, None, 6, 11, 0, 527, None),
 (23176594, None, 0, 23, 6, 489, None),
 (26742952, None, 1, 7, 4, 478, None),
 (22283104, None, 0, 22, 0, 406, None),
 (42558192, None, 2, 10, 0, 396, None)]

# pp(top_ten)

#result = server.update_ranking(workid=44044893, rank=2)
# print(result)

if __name__ == "__main__":
    main(timestamp=timestamp)