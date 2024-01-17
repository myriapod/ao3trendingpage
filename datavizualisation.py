from packages.ao3tosql import AO3toSQL
from pprint import pp
import sys

def main(timestamp):
    AO3session = AO3toSQL(timestamp)
    ao3session = AO3session.ao3_connect()

    top_ten=[(52783675, None, 5, 63, 4, 1525, None),
    (51925780, None, 26, 31, 7, 1415, None),
    (50329543, None, 9, 36, 2, 1308, None),
    (42918813, None, 47, 13, 3, 1050, None),
    (52571257, None, 11, 37, 2, 972, None),
    (51141283, None, 9, 27, 4, 774, None),
    (50723278, None, 23, 20, 1, 765, None),
    (43355023, None, 1, 8, 3, 755, None),
    (52675660, None, 11, 83, 11, 747, None),
    (44044893, None, 0, 9, 2, 645, None)]

    top_ten_crossover = [(24620431, None, 8, 39, 1, 1613, None),
    (50941855, None, 17, 32, 1, 781, None),
    (47507560, None, 16, 26, 6, 742, None),
    (20176075, None, 1, 19, 1, 668, None),
    (27002017, None, 17, 28, 5, 588, None),
    (44044893, None, 6, 11, 0, 527, None),
    (23176594, None, 0, 23, 6, 489, None),
    (26742952, None, 1, 7, 4, 478, None),
    (22283104, None, 0, 22, 0, 406, None),
    (42558192, None, 2, 10, 0, 396, None)]

    for work in top_ten:
        pp(AO3session.ao3_workid_search(work[0]))

if __name__ == "__main__":
    timestamp = ' '.join([sys.argv[1], sys.argv[2]])
    main(timestamp=timestamp)