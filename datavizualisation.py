from packages.ao3api import AO3API
from pprint import pp

AO3session = AO3API()
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

for work in top_ten:
    pp(AO3session.ao3_work_search(work[0]))