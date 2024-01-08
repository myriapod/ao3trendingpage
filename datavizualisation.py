from packages.ao3tosql import Search

data_format = {"authors": "",
                "categories": "",
                "characters": "",
                "complete": "",
                "expected_chapters": "",
                "fandoms": "",
                "language": "",
                "nchapters": "",
                "rating": "",
                "relationships": "",
                "restricted": "",
                "series": "",
                "status": "",
                "summary": "",
                "tags": "",
                "title": "",
                "warnings": "",
                "words": "",
                "id": "",
                }

"""work = AO3.Work(workid=id)

workdata = deepcopy(data_format)

for key in work.metadata.keys():
    if key in workdata.keys():
        workdata[key] = work.metadata[key]"""