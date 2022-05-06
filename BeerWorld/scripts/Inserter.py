from itertools import count
from types import coroutine
from webbrowser import get
import psycopg2
from random import choice
from string import digits
import random
import datetime

def get_random_str(countOfWarehouse): # количество складов 
    universaryCode = []
    for i in range(0, countOfWarehouse):
        str = ''.join(choice(digits) for i in range(10)) 
        universaryCode.append(str)
    return universaryCode


try:
        
    conn = psycopg2.connect(database="beerWorld",  host="localhost", port=5432)
    conn.autocommit=False
    cur = conn.cursor()

    cur.execute('INSERT INTO "Brewery" (name, country, year) VALUES (%s, %s, %s)',
        (name,
        cntry,
        str(years))
        )

except (Exception, psycopg2.DatabaseError) as error :
    print ("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
    conn.rollback()
finally:
    conn.commit()
    if conn:
        cur.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")


   