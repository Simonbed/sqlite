import sqlite3
import io
import csv

#Creating the Database
conn = sqlite3.connect('sql_trial.sqlite')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Economics''')

#We create tables for our database.
cur.execute('''CREATE TABLE IF NOT EXISTS Economics
    (id INTEGER PRIMARY KEY,  CPICANADARTE FLOAT, DATE_LIST TEXT)''')

gdplist = list()

# From csv files, we will create lists to insert the data into the database
with open('CPICADRTE.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row[0]) #We used print only to see what we had
        #print(row) #Same thing, only to see what data we have -- Make sure the data is what we thought
        if row[0] == "DATE":
            continue
        else:
            gdplist.append(row)


count = 0
for row in gdplist :
    try:
        gdp = gdplist[count]
    except:
        gdp = 'null', 'NULL'

    cur.execute('''INSERT INTO Economics (CPICANADARTE, DATE_LIST) VALUES (?,?)''', (gdp[1], gdp[0]))
    count = count + 1


conn.commit()
cur.close()
