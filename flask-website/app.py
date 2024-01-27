from ..packages.sqlserver import SQLServer
from flask import Flask, render_template

sqlserver = SQLServer()
sqlserver.connection()
data = sqlserver.get_ranking()