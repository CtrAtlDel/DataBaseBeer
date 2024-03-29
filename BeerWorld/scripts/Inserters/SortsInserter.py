import psycopg2
from random import choice, randint
import string    
import random 


def get_random_str(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length)) 

try:
        
    conn = psycopg2.connect(database="beerWorld",  host="localhost", port=5432)
    conn.autocommit=False
    cur = conn.cursor()

    sorts = ['Ale', 'Lager', 'Porter', 'Stout', 'Blonde Ale', 'Brown Ales', 'Pale Ale',
        'Wheat', 'Pilsner', 'Sour Ale', 'Russian', 'zxc', 'IPA']

    for i in range(0, 9990):
        cur.execute('INSERT INTO "Sort"(sort_name) VALUES (%s)',[str(get_random_str(10))])

except (Exception, psycopg2.DatabaseError) as error :
    print ("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
    conn.rollback()
finally:
    conn.commit()
    if conn:
        cur.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")