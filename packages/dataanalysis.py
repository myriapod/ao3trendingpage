from sqlserver import SQLServer
import sys
from progressbar import printProgressBar

def main(timestamp):
    server = SQLServer()
    server.connection()
    list_workid = server.get_list_workid()
    
    iter=0
    for workid in list_workid:
        iter += 1
        last_two=server.get_last_two(workid)
        if len(last_two)>1:
            commentsDiff = last_two[0][4]-last_two[1][4]
            kudosDiff = last_two[0][5]-last_two[1][5]
            bookmarksDiff = last_two[0][6]-last_two[1][6]
            hitsDiff = last_two[0][7]-last_two[1][7]
            server.update_stats(workid, commentsDiff, kudosDiff, bookmarksDiff, hitsDiff)
        else:
            server.update_stats(workid, last_two[0][4], last_two[0][5], last_two[0][6], last_two[0][7])
        printProgressBar(iteration=iter, total=len(list_workid), prefix=f"Data analysis progress: ")
    
    top_ten = server.get_top_10(crossover=False) # consider fandom specific top 10
    # only works on ATEEZ for now

    i=1
    for top in top_ten:
        server.update_ranking(workid=top[0], fandom_name="ATEEZ", rank=i, timestamp=timestamp)
        i+=1
    server.update_out_of_ranking(timestamp)

if __name__ == "__main__":
    timestamp = ' '.join([sys.argv[1], sys.argv[2]])
    main(timestamp=timestamp)