# pylint: disable=too-many-instance-attributes,invalid-name,unspecified-encoding, unused-wildcard-import
# pylint: disable=too-few-public-methods,attribute-defined-outside-init,no-member,consider-using-dict-items
"""Reads files and saves them into the specified database"""
import os
import re
import sqlite3
import sys

if os.path.exists('files.db'):
    os.remove('files.db')

conn = sqlite3.connect('files.db')
cur = conn.cursor()
cur.execute('CREATE TABLE files (ext, path, fname)')
absp = os.path.abspath(sys.argv[1])[:-5]
for (root, dirs, files) in os.walk(sys.argv[1], topdown=True):
    for i in files:
        if i[:1] == '.' or i[:1] == '-':
            pass
        else:
            try:
                ft = re.search(r'(?<=\.)(.*)', i).group()
            except AttributeError:
                ft = ''
            if ft == '':
                pass
            else:
                cur.execute(f'INSERT INTO files VALUES (\'{ft}\', \'{absp}{root}\', \'{i}\')')
conn.commit()
cur.execute('select * from files')
rows = cur.fetchall()

with open('files-part1.txt', 'w') as f:
    for row in rows:
        # print(row)
        f.write(f'{str(row)}\n')
conn.close()
print('filesdb created')
