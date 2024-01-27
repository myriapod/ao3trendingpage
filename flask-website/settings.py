from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MDBUSER=environ.get('MDBUSER')
MDBPWD=environ.get('MDBPWD')
DATABASE=environ.get('DATABASE')
TABLEDATA=environ.get('TABLEDATA')
TABLEID=environ.get('TABLEID')
TABLERANK=environ.get('TABLERANK')
SQLHOST=environ.get('SQLHOST')
AO3USER=environ.get('AO3USER')
AO3PWD=environ.get('AO3PWD')
AO3WAITINGTIME=environ.get('AO3WAITINGTIME')