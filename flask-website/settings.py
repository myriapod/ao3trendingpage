import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MDBUSER=os.environ.get('MDBUSER')
MDBPWD=os.environ.get('MDBPWD')
DATABASE=os.environ.get('DATABASE')
TABLEDATA=os.environ.get('TABLEDATA')
TABLEID=os.environ.get('TABLEID')
TABLERANK=os.environ.get('TABLERANK')
SQLHOST=os.environ.get('SQLHOST')
AO3USER=os.environ.get('AO3USER')
AO3PWD=os.environ.get('AO3PWD')
AO3WAITINGTIME=os.environ.get('AO3WAITINGTIME')
AO3TIMESTAMP=os.environ.get("AO3TIMESTAMP")