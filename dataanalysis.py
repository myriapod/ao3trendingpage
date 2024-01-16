from packages.sqlimport import SQLServer
from pprint import pp


server = SQLServer()
server.connection()
list_workid = server.get_list_workid()

for workid in list_workid:
    last_two=server.get_last_two(workid)
    try:
        commentsDiff = last_two[0][4]-last_two[1][4]
        kudosDiff = last_two[0][5]-last_two[1][5]
        bookmarksDiff = last_two[0][6]-last_two[1][6]
        hitsDiff = last_two[0][7]-last_two[1][7]
        server.update_stats(workid, commentsDiff, kudosDiff, bookmarksDiff, hitsDiff)
    #print(commentsDiff, kudosDiff, bookmarksDiff, hitsDiff)
    except IndexError as err: # maybe here put the workids in a file or add a tag to the ranking column
        print(err, f"Error for - {workid} - possibly the first entry for the fic")
        with open("logs.txt", "a") as logs:
            logs.write(f"Error for - {workid} - possibly the first entry for the fic")

top_ten = server.get_top_10(crossover=False)
pp(top_ten)