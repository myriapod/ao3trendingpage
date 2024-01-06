CREATE TABLE stats 
(
    id int auto_increment PRIMARY KEY,
    fandom varchar(250),
    workid int,
    timestamp timestamp,
    comments int,
    kudos int,
    bookmarks int,
    hits int,
    date_edited date,
    date_published date,
    date_updated date);