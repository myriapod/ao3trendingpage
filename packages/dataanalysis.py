from sqlserver import SQLServer
import sys
from datetime import datetime, date

def main(timestamp):
    server = SQLServer()
    server.connection()
    list_workid = server.get_list_workid()
    
    iter=0
    for workid in list_workid:
        iter += 1
        last_two=server.get_last_two(workid)
        
        if len(last_two)>1:
            commentsDiff = (last_two[0]["comments"]-last_two[1]["comments"])*3
            kudosDiff = (last_two[0]["kudos"]-last_two[1]["kudos"])*4
            bookmarksDiff = (last_two[0]["bookmarks"]-last_two[1]["bookmarks"])*2
            hitsDiff = last_two[0]["hits"]-last_two[1]["hits"]
            
            freshnessdelta = date.today() - max(last_two[0]["date_edited"], last_two[0]["date_published"], last_two[0]["date_updated"])
            freshness = freshnessdelta.days

            score = (commentsDiff+kudosDiff+bookmarksDiff+hitsDiff) - (freshness)
            
            server.update_stats(workid, commentsDiff, kudosDiff, bookmarksDiff, hitsDiff, score)
        
        else:
            freshnessdelta = date.today() - max(last_two[0]["date_edited"], last_two[0]["date_published"], last_two[0]["date_updated"])
            freshness = freshnessdelta.days

            score = (last_two[0]["comments"] + last_two[0]["kudos"] + last_two[0]["bookmarks"] + last_two[0]["hits"]) - (freshness)

            server.update_stats(workid, last_two[0]["comments"], last_two[0]["kudos"], last_two[0]["bookmarks"], last_two[0]["hits"], score)

        print(f'{timestamp} - Entered analyzed data for work {workid}')
        print("Progress = "+ "{:.2f}".format(100 * (iter / float(len(list_workid)))))
    
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