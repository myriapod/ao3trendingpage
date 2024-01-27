from flask import Flask, render_template
from ao3workfetch import ao3workfetch

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('settings.py')

@app.route('/')
def index():
    data = ao3workfetch(manual_env=[app.config["MDBUSER"], app.config["MDBPWD"], app.config["SQLHOST"], app.config["DATABASE"], app.config["TABLEDATA"], app.config["TABLEID"], app.config["TABLERANK"]])


    return render_template('index.html', ranking=data)