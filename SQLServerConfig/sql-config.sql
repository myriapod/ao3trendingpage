CREATE TABLE stats (   
    id int auto_increment PRIMARY KEY,
    fandom varchar(250),
    workid int,
    timestmp timestamp,
    crossover bool,
    comments int,
    kudos int,
    bookmarks int,
    hits int,
    date_edited date,
    date_published date,
    date_updated date
);

CREATE TABLE workid (
    workid int PRIMARY KEY,
    ranking int,
    commentsDiff int,
    kudosDiff int,
    bookmarksDiff int,
    hitsDiff int,
    keyword varchar(50)
);

CREATE TABLE ranking (
    workid int PRIMARY KEY,
    fandom varchar(50),
    ranking int,
    timestmp timestamp,
    keyword varchar(50),
    worktitle varchar(250),
    authors varchar(250),
    relationship varchar(250),
    chapters varchar(250),
    latest_updated varchar(250),
    categories varchar(250),
    tags varchar(250),
    words int
);