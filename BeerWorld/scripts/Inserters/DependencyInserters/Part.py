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

    cur.execute('SELECT id_brewery FROM "Brewery"')
    id_brewery = [id[0] for id in cur.fetchall()]

    for i in range(0, 10_000):
        cur.execute('INSERT INTO "Part" (id_brewery, size_part) VALUES (%s, %s)',
            (random.choice(id_brewery),
            randint(1, 10))
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