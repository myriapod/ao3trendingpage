# ao3trendingpage
Data engineering personal project that displays a trending page for AO3 fics of a specific fandom.

<h3>Current status</h3>
- ran one time from extraction to analysis, updating the top10.json file

<h3>To do</h3>
- hosting the sql database in the cloud (azure?)
- connecting with the cloud hosted database
- docker container + cronjob to run the data extraction once a day (on own raspberry pi server?)
- web interface
- data cleanup

<h1>How to</h1>

create a .env file in the packages folder to hold the variables:
<code>
AO3USER=
AO3PWD=
MDBUSER=
MDBPWD=
DATABASE=ao3trendingpage
TABLEDATA=stats
TABLEID=workid
TABLERANK=ranking
SQLHOST=
AO3WAITINGTIME=240</code>

run the <code>main.sh</code> file to get everything working

the database is defined in the sql-config.sql file


<h1>To do:</h1>
rework the ranking database so that it can store metadata about the top 10 (only)