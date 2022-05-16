from re import L
import re
import psycopg2
from random import choice, randint
import string    
import random 


def get_random_str(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length)) 

def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)    

def get_random_point():
    x = randint(0, 20)
    y = randint(0, 20)
    return ''.join('(' + str(x) +',' + str(y) + ')')


try:
        
    conn = psycopg2.connect(database="beerWorld",  host="localhost", port=5432)
    conn.autocommit=False

    cur = conn.cursor()

    for i in range(0, 10000):
        cur.execute('INSERT INTO "WareHouse" (university_code, address, capacity, phone_number, boss, information, coordinates) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)',
            [get_random_str(10),
            str(get_random_str(12)),
            str(randint(500, 3000)),
            str(random_phone_num_generator()),
            str(get_random_str(7)),
            get_random_str(6),
            str(get_random_point())]
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