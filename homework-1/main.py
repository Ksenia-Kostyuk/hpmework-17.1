import csv
import psycopg2

with psycopg2.connect(host="localhost",
                      port='1024',
                      dbname="north",
                      user="postgres",
                      password="12345") as conn:
    with conn.cursor() as cur:
        with open('north_data\\employees_data.csv', 'r', encoding='latin1') as csvfile:
            pass_line = next(csvfile)
            data = csv.reader(csvfile)
            for info in data:
                query = "INSERT INTO employees VALUES(%,%,%,%,%)"
                cur.execute(query, info)
                cur.fetchall()
conn.close()

with psycopg2.connect(host="localhost",
                      port='1024',
                      dbname="north",
                      user="postgres",
                      password="12345") as conn:
    with conn.cursor() as cur:
        with open('north_data\\customers_data.csv', 'r', encoding='latin1') as csvfile:
            pass_line = next(csvfile)
            data = csv.reader(csvfile)
            for info in data:
                query = "INSERT INTO employees VALUES(%,%,%)"
                cur.execute(query, info)
                cur.fetchall()
conn.close()

with psycopg2.connect(host="localhost",
                      port='1024',
                      dbname="north",
                      user="postgres",
                      password="12345") as conn:
    with conn.cursor() as cur:
        with open('north_data\\orders_data.csv', 'r', encoding='latin1') as csvfile:
            pass_line = next(csvfile)
            data = csv.reader(csvfile)
            for info in data:
                query = "INSERT INTO employees VALUES(%,%,%,%,%)"
                cur.execute(query, info)
                cur.fetchall()
conn.close()


