"""
Script used to create a DB from the patchwork email subject data dump.

By Alex Courouble
"""
import sqlite3
INPUT_FILE_PATH = '~/Desktop/email2git_data/subject/pwSubject.txt'
DB_PATH = '~/Desktop/email2git_data/pwSubject.db'


table = []

with open(INPUT_FILE_PATH,"r") as s:
	for i in s.read().split('\n'):
		patchData = i.split("\t")
		patchId = patchData[0] 
		patchSubject =  patchData[1]
		# print patchId,"	",patchSubject
		table.append((patchId,patchSubject))

conn = sqlite3.connect(DB_PATH) # connecting
conn.text_factory = str
c = conn.cursor() #creating cursor
c.execute('''create table subject(pwid int, subject text)''') # creating the table
c.executemany('INSERT INTO subject VALUES (?,?)', table) # importing all the data
conn.commit()
conn.close() # we're done!