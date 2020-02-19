from os import getenv
import sqlite3
import binascii
conn = sqlite3.connect("....../Cookies") #路径
cursor = conn.cursor()
cursor.execute('SELECT name,value,encrypted_value FROM cookies')
for result in cursor.fetchall():
    print(binascii.b2a_hex(result[2]))
    f = open('test.txt','wb')
    f.write(result[2])
    f.close()

