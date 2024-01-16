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

ALTER TABLE workid ADD COLUMN ranking int, ADD COLUMN commentsDiff int, ADD COLUMN kudosDiff int, ADD COLUMN bookmarksDiff int, ADD COLUMN hitsDiff int, ADD COLUMN keyword varchar(50);

ALTER TABLE stats ADD COLUMN crossover bool;

CREATE TABLE ranking (
    workid int PRIMARY KEY,
    ranking int,
    timestmp timestamp,
    keyword varchar(50)
);


INSERT (commentsDiff, kudosDiff, bookmarksDiff, hitsDiff) INTO workid VALUES 244, 2, 10, 50 WHERE workid.workid=52902139;
INSERT (commentsDiff, kudosDiff, bookmarksDiff, hitsDiff) INTO workid VALUES 44, 233, 54, 3 WHERE workid.workid=52895290;
INSERT (commentsDiff, kudosDiff, bookmarksDiff, hitsDiff) INTO workid VALUES 442, 233, 54, 3433 WHERE workid.workid=52854073;