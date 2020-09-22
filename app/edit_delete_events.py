
import psycopg2

con = psycopg2.connect(dbname='weather_forecast_dev', user='postgres',
password='docker',host='localhost')




def sql_update(con):

    cursorObj = con.cursor()

    # cursorObj.execute("UPDATE events SET theme = '' where _id = 1;")

    con.commit()

sql_update(con)


def sql_fetch(con):

    cursorObj = con.cursor()

    # cursorObj.execute('SELECT * FROM events')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)
