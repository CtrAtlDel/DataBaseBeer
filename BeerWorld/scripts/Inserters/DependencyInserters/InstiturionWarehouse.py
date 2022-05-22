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

    cur.execute('SELECT id_wareHouse FROM "WareHouse"') # id_wareHouse
    id_wareHouse = [id[0] for id in cur.fetchall()]

    cur.execute('SELECT id_institution FROM "Institution"') # id_institution
    id_institution = [id[0] for id in cur.fetchall()]


    for i in range(0, 9000):
        cur.execute('INSERT INTO "InstitutionWarehouse" (id_wareHouse, id_institution) VALUES (%s, %s)',
            (random.choice(id_wareHouse),
            random.choice(id_institution))
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