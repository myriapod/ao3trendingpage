from packages.sqlserver import SQLServer
import sys

def main(timestamp):
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
            with open("packages/logs.txt", "a") as logs:
                logs.write(f"{timestamp} - Error for - {workid} - possibly the first entry for the fic\n")

    top_ten = server.get_top_10(crossover=False) # consider fandom specific top 10
    # only works on ATEEZ for now

    i=1
    for top in top_ten:
        server.update_ranking(workid=top[0], fandom_name="ATEEZ", rank=i, timestamp=timestamp)
        i+=1
    
    
    server.json_dump(str("packages/top10.json"))

if __name__ == "__main__":
    timestamp = ' '.join([sys.argv[1], sys.argv[2]])
    main(timestamp=timestamp)