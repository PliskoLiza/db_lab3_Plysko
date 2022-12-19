import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '1234'
database = 'Lab_2_DB'
host = 'localhost'
port = '5432'

query_1 = '''
create view OscarsTotal as
SELECT film_name, quantity FROM 
(filmawards INNER JOIN film ON film.film_id = filmawards.film_id)
'''

query_2 = '''
create view GenresCount as
SELECT genre_name, Count(filmgenres.film_id) as quantity 
FROM (filmgenres INNER JOIN genres ON filmgenres.genre_id = genres.genre_id)
GROUP BY genres.genre_name ORDER BY quantity
'''

query_3 = '''
create view FilmYears as
SELECT COUNT(film_name) as quantity, extract(year from release_date) as year 
FROM Film GROUP BY year ORDER BY year
'''



conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute('DROP VIEW IF EXISTS OscarsTotal')

    cur.execute(query_1)

    cur.execute('SELECT * FROM OscarsTotal')
    oscars = []
    films_1 = []

    for row in cur:
        films_1.append(row[0])
        oscars.append(row[1])

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    x_range = range(len(oscars))
    bar_ax.bar(x_range, oscars, label='Count')
    bar_ax.set_title('Кількість Оскарів')
    bar_ax.set_xlabel('Фільми')
    bar_ax.set_ylabel('Кількість')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(films_1, rotation=45, ha='right')

    cur.execute('DROP VIEW IF EXISTS GenresCount')

    cur.execute(query_2)

    cur.execute('SELECT * FROM GenresCount')
    films_2 = []
    total = []

    for row in cur:
        films_2.append(row[0])
        total.append(row[1])
    pie_ax.pie(total, labels=films_2, autopct='%1.1f%%')
    pie_ax.set_title('Частка фільмів кожного жанру')

    cur.execute('DROP VIEW IF EXISTS FilmYears')

    cur.execute(query_3)

    cur.execute('SELECT * FROM FilmYears')
    quantity = []
    year = []

    for row in cur:
        quantity.append(row[0])
        year.append(row[1])

    graph_ax.plot(year, quantity, marker='o')
    graph_ax.set_xlabel('Рік виходу')
    graph_ax.set_ylabel('Кількість')
    graph_ax.set_title('Графік залежності кількості фільмів, від року')

    for qnt, yr in zip(quantity, year):
        graph_ax.annotate(yr, xy=(qnt, yr), xytext=(7, 2), textcoords='offset points')

mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()
