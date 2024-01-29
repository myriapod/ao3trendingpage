from flask import Flask, render_template
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'packages'))
from ao3tosql import AO3toSQL #type: ignore

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('settings.py')

@app.route('/')
def index():
    # the manual_env kind of sucks, it's a working work around but it's not very pretty
    ao3 = AO3toSQL(timestamp=None) # no need for the timestamp at this stage
    data = ao3.sqlserver.get_ranking_for_html()
    timestamp = ao3.sqlserver.get_timestamp_for_html()

    category_table = {
        "M/M": "slash",
        "F/M": "het",
        "F/F": "femslash",
        "Multi": "multi",
        "Other": "other",
        "N/A": "none",
        "Gen": "gen"
    }
    rating_table = {
        "Mature": "mature",
        "Not Rated": "notrated",
        "Explicit": "explicit",
        "Teen And Up Audiences": "teen",
        "General Audiences": "general-audience"
    }

    return render_template('index.html', ranking=data, timestamp=timestamp, category_table=category_table, rating_table=rating_table)