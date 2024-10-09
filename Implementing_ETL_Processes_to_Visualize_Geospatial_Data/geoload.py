'''
Script to construct URLs which request geospatial coordinates from a proxy of the GeoAPI API. Then, cache these location and coordinate data into a SQLite database.
'''

import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

#URL to a proxy of the GeoAPI API.
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Loop to parse a text file containing location names(where.data). Encoded these location names into a URL format and concatenated them with the proxy API URL(serviceurl). Used these constructed URLs to request geospatial data for each corresponding location name and inserted these data into a SQLite database. 
fh = open("where.data")
count = 0
nofound = 0
for line in fh:
    if count > 100 :
        print('Retrieved 100 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue
    except:
        pass

    parms = dict()
    parms['q'] = address
    
    #Concatenating proxy URL with URL encoded location name.
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1
    
    #Error checking.
    try:
        js = json.loads(data)
    except:
        print(data)  #Print in case unicode causes an error.
        continue

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1
    
    #Inserting data into SQLite database.
    cur.execute('''INSERT INTO Locations (address, geodata)
        VALUES ( ?, ? )''',
        (memoryview(address.encode()), memoryview(data.encode()) ) )

    conn.commit()

    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)
#Print the number of geospatial coordinate data not found from the proxy API request.
if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database to visualize it on a map.")

