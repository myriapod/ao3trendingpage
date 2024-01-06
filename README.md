# ao3trendingpage
Data engineering project that displays a trending page for AO3 fics

<h1>Data extraction</h1>

<h2>AO3 API Python script</h2>
/data-extraction/main contains the code to connect to the AO3 API and fetch all of the works per fandom researched with a timestamp attached to them.
The list of fandoms searched can be found at /data-extraction/fandom_list.txt

After webscrapping is done, the results are stored in a MariaDB database.

<h1>Data storage</h1>
<h2>MariaDB database structure</h2>

<h3>Stats table</h3>
This table is updated every time the python script runs. The work IDs appear several times, with a different timestamp and stats to track the trends. Each entry has an autoincremented ID in this table to falicitate chronologisation.

<b>issue :</b> mariadb.OperationalError: FUNCTION datetime.datetime does not exist. Check the 'Function Name Parsing and Resolution' section in the Reference Manual (str(date) but it didn't help)

<h2>Store the SQL database on AZURE</h2>
<b>to do</b>

<h1>Data analysis</h1>

Group-by every work ID on the stats table
Compare the last 2 entries for a single work ID
Store the difference and the work ID
Get the top 10 biggest differences with the work ID

<h1>Data vizualisation</h1>

- Python script that uses the AO3 API to fetch the metadata from the work IDs in the trending page
- Q: Could it be in Javascript/Typescript to allow a web interface

<h1>Data cleanup</h1>
Once a day, remove all the entries from the stats table when the amount of entries for the same fic is bigger than 7 (a week if we're doing it daily), remove the oldest entries.


