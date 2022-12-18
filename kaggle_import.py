import csv
import psycopg2

username = 'postgres'
password = '1234'
database = 'Lab_3_DB'

INPUT_CSV_FILE = 'imdb_top250_movies.csv'

delete_all = '''
DELETE FROM filmawards;
DELETE FROM filmgenres;
DELETE FROM filmrating;
DELETE FROM film;

DELETE FROM genres;
'''

query_filmawards = '''
INSERT INTO filmawards (film_id, award_id, quantity) VALUES (%s, %s, %s)
'''

query_filmgenres = '''
INSERT INTO filmgenres (film_id, genre_id) VALUES (%s, %s)
'''

query_genres = '''
INSERT INTO genres (genre_id, genre_name) VALUES (%s, %s)
'''

query_film = '''
INSERT INTO film (film_id, film_name, release_date, runtime, production) VALUES (%s, %s, %s, %s, %s)
'''

query_filmrating = '''
INSERT INTO filmrating (film_id, platform_id, rating_date, rating) VALUES (%s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

def find_count(s):
    word_list = s.split()
    for i in word_list:
        if i.isnumeric():
            return i
    return 0

def filmgenres_insert(local_film_id, local_row, local_cur):
    local_genres = local_row.split(',')
    for j in range(0, len(local_genres)):
        local_cur.execute(query_filmgenres, (local_film_id, local_genres[j].strip()))


def genres_insert(local_row, local_cur, genres):
    local_genres = local_row.split(',')
    for j in local_genres:
        if genres.count(j.strip()) == 0:
            genres.append(j.strip())
            local_cur.execute(query_genres, (j.strip(), j.strip()))


def film_insert(local_film_id, local_title, local_data, local_runtime, local_production, reserve_year, local_cur):
    if local_data == "":
        local_data = "01.01." + reserve_year
    local_cur.execute(query_film, (local_film_id, local_title, local_data, local_runtime.partition(' ')[0], local_production))


def filmrating_insert(local_film_id, local_imdb_rating, local_metascore_rating, local_cur):
    if local_metascore_rating != '':
        local_cur.execute(query_filmrating, (local_film_id, 'Metascore', "18.12.2022", local_metascore_rating))
    if local_imdb_rating != '':
        local_cur.execute(query_filmrating, (local_film_id, 'IMDb', "18.12.2022", local_imdb_rating))
    return


def filmawards_insert(local_film_id, local_awards, local_cur):
    if local_awards.find("BAFTA") != -1:
        local_cur.execute(query_filmawards, (local_film_id, 'BAFTA', find_count(local_awards)))
    elif local_awards.find("Golden Globe") != -1:
        local_cur.execute(query_filmawards, (local_film_id, 'Golden Globe', find_count(local_awards)))
    else:
        local_cur.execute(query_filmawards, (local_film_id, 'Oscar', find_count(local_awards)))


with conn:
    cur = conn.cursor()
    cur.execute(delete_all)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        genres = []
        for idx, row in enumerate(reader):
            genres_insert(row['Genre'], cur, genres)
            film_insert(row['Num'], row['Title'], row['Released'], row['Runtime'], row['Production'], row['Year'], cur)
            filmgenres_insert(row['Num'], row['Genre'], cur)
            filmrating_insert(row['Num'], row['imdbRating'], row['Metascore'], cur)
            filmawards_insert(row['Num'], row['Awards'], cur)
    conn.commit()