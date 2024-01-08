CREATE TABLE stats (   
    id int auto_increment PRIMARY KEY,
    fandom varchar(250),
    workid int,
    timestmp timestamp,
    comments int,
    kudos int,
    bookmarks int,
    hits int,
    date_edited date,
    date_published date,
    date_updated date
);

CREATE TABLE workid (
    workid int PRIMARY KEY
);