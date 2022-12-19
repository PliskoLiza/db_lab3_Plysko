import json
import psycopg2

username = 'postgres'
password = '1234'
database = 'Lab_3_DB'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:
    cur = conn.cursor()

    for table in ('film', 'filmawards', 'filmgenres', 'filmrating', 'genres', 'rating_platforms', 'awards'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('all_data_lab_3.json', 'w') as outf:
    json.dump(data, outf, default=str)