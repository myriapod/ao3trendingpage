# ao3trendingpage
Personal project that displays a trending page for AO3 fics of a specific fandom.

<h2>Current stage</h2>

- Works on self host
- Flask website is up
- Only works for the ATEEZ fandom

<h2>Set up</h2>
<h3>1. Complete <code>.env</code> file</h3>

Especially for variables <code>AO3USER</code> and <code>AO3PWD</code> (your username and password for AO3 sessions). The rest are filled in with a default value, that you can also change.
Watch out for the <code>MDBUSER</code> and <code>MDBPWD</code> that are defaulted, when you need to set up mariadb.

<h3>2. Run <code>main.sh</code></h3>

<code>main.sh</code> should be all you need to run to set everything up.

<h4>Troubleshooting:</h4>

If you encounter an error when running <code>main.sh</code> involving the number of total results that contain a ",", you should modify the package files for the AO3_api as such:

<code>file: AO3/search.py, line 112:</code>
<code>self.total_results = int(maindiv.find("h3", {"class": "heading"}).getText().strip().split(" ")[0].replace(',',''))</code>