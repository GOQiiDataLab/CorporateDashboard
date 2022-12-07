import pymysql
import json

with open('Credetials.json','r') as f:
    data = json.load(f)

def database():

    return pymysql.connect(host=data['server_goqii'],
                                 user=data['username'],
                                 passwd=data['password'],
                                 db=data['goqii_database'],
                                 charset='utf8'
                                 )
