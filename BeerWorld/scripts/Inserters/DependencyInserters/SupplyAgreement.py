import psycopg2
from random import choice, randint
import string    
import random 
from main import 


def get_random_str(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))  

try:
        
    conn = psycopg2.connect(database="beerWorld",  host="localhost", port=5432)
    conn.autocommit=False
    cur = conn.cursor()

    arr_account = set()
    arr_cost = set()
    arr_count = []
    for i in range(0, 10000):
        account_number = get_random_str(20)
        cost = randint(1, 5000)
        arr_cost.add(cost)
        arr_count = randint(1, 5000)
        arr_account.add(account_number)
        cur.execute('INSERT INTO "SupplyAgreement"(id_institution, name_beer, \
                        container, count_of_beer, cost, start_date, account_number, \
                        prepayment, name_of_institution, delivery_period, count_of_delivery, isImporter) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (randint(1, 10000),
            random.choice(),
            random.choice(),
            randint(1, 10000),
            cost,
            '1997-08-24',
            account_number,
            random.choice(arr_account),
            random.choice(),
            '40:00:00',
            randint(1, 100),
            random.choice([True, False]),
            )
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