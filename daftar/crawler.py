import json
import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

parsed = json.loads('datas.json')
print(json.dumps(parsed, indent=4))