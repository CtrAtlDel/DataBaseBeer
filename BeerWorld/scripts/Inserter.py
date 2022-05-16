
import psycopg2
from random import choice
from string import digits
from Beer import beerNames


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

    brewery = getBreweryes()
    
    j = 0
    for i in range(3, len(beerNames)):
        j += 1
        id_part = i
        id_brewery = i
        cur.execute('INSERT INTO "Beer"(id_part, id_brewery, name_of_beer, container, drinkAbility, description, color, strength, volume,\
                    price_purchase, price_selling, price_wholesale, sort)\
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (name,
        cntry,
        str(years))
        )


    # Example of instertinh
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


   