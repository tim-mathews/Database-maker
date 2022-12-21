# pylint: disable=too-many-instance-attributes,invalid-name,unspecified-encoding, unused-wildcard-import
# pylint: disable=too-few-public-methods,attribute-defined-outside-init,no-member,consider-using-dict-items
"""Gathers files from a database"""
import zipfile
import sqlite3
import sys


conn = sqlite3.connect(sys.argv[1])
cur = conn.cursor()
fe = {}

args = [*sys.argv[2:]]
for i in args:
    cur.execute(f'select * from files where ext like \'{i}\'')
    rows = cur.fetchall()
    fe[i] = len(rows)
    with zipfile.ZipFile(f'{i}.zip', 'w', zipfile.ZIP_DEFLATED) as zfile:
        for item in rows:
            zfile.write(item[1] + '\\' + item[2])

for i in fe:
    print(f'{fe[i]} {i} files gathered')
