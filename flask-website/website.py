from flask import Flask, render_template
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'packages'))
from ao3tosql import AO3toSQL #type: ignore

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('settings.py')

@app.route('/')
def index():
    # the manual_env kind of sucks, it's a working work around but it's not very pretty
    manual_env={"MDBUSER": app.config["MDBUSER"], 
                "MDBPWD" : app.config["MDBPWD"], 
                "SQLHOST": app.config["SQLHOST"], 
                "DATABASE": app.config["DATABASE"], 
                "TABLEDATA": app.config["TABLEDATA"], 
                "TABLEID": app.config["TABLEID"], 
                "TABLERANK": app.config["TABLERANK"],
                "AO3USER": app.config["AO3USER"],
                "AO3PWD": app.config["AO3PWD"]}
    ao3 = AO3toSQL(timestamp="", manual_env=manual_env) # no need for the timestamp at this stage
    data = ao3.sqlserver.get_ranking_for_html()

    return render_template('index.html', ranking=data)