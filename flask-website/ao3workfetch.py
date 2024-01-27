import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'packages'))
from ao3tosql import AO3toSQL

def ao3workfetch(manual_env):
    ao3 = AO3toSQL(timestamp="", manual_env=manual_env)
    data = ao3.sqlserver.get_ranking()
    
    for entry in data:
        meta = ao3.ao3_workid_search(data[entry]["workid"])
        data[entry]["worktitle"] = meta["title"]
        data[entry]["author"] = ' & '.join(meta["authors"])
        data[entry]["relationship"] = meta["relationships"][0]
        if meta["expected_chapters"] == None:
            data[entry]["chapters"] = f'{meta["nchapters"]}/?'
        else:
            data[entry]["chapters"] = f'{meta["nchapters"]}/{meta["expected_chapters"]}'
        data[entry]["latest_updated"] = meta["date_updated"].split(" ")[0]
        data[entry]["categories"] = ', '.join(meta["categories"])
        data[entry]["tags"] = ', '.join(meta["tags"][:4])
        data[entry]["words"] = meta["words"]

    return data