from calendar import c
from html.entities import name2codepoint
from pydoc import describe
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

def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

sorts = ['Ale', 'Lager', 'Porter', 'Stout', 'Blonde Ale', 'Brown Ales', 'Pale Ale',
         'Wheat', 'Pilsner', 'Sour Ale', 'Russian', 'zxc', 'IPA']
typeInstitution = ['restaurant', 'bar', 'snack-bar']
statusInstitution = ['the best', 'middle', 'not so bad']
trackingOrder = ['inBrewery', 'inWareHouse', 'inInstitution']
typePayment = ['cash', 'online']
beerContainer = ['bottle', 'barrel', 'tank', 'keg']
drinkAbility = ['Good', 'Execelent', 'Middle', 'Not so bad']
discription = 'description'
color = ['Mash', 'Roasted Malts', 'Fermentation', 'Cold Break']

strength = [3, 4, 5, 6, 9]
volume = [1, 5, 10, 100]

try:
        
    conn = psycopg2.connect(database="beerWorld",  host="localhost", port=5432)
    conn.autocommit=False

    cur = conn.cursor()

    statusInstitution = ['the best', 'middle', 'not so bad']
    typeInstitution = ['restaurant', 'bar', 'snack-bar']

    #Dependency

    #SortBrewery
    for i in range(0, 5000):
        cur.execute('INSERT INTO "SortBrewery" (id_sort, id_brewery) VALUES (%s, %s)',
            (randint(1, 5000),
            randint(1,5000))
        )
    #InstutionWarehouse
    for i in range(0, 5000):
        cur.execute('INSERT INTO "InstitutionWarehouse" (id_wareHouse, id_institution) VALUES (%s, %s)',
            (randint(1, 10000),
            randint(1,10000))
        )
    
    #Part 
    for i in range(0, 5000):
        cur.execute('INSERT INTO "Part" (id_brewery, size_part) VALUES (%s, %s)',
            (randint(1, 10000),
            randint(1,10))
        )
    
    #HalfPart
    for i in range(0, 5000):
        cur.execute('INSERT INTO "HalfPart" (id_wareHouse, id_part, id_brewery, size_half) VALUES (%s, %s, %s, %s)',
            (randint(1, 10000),
            randint(1, 10000)),
            randint(1, 10000),
            randint(1, 10)
        )

    #Beer
    arr_beer = set()
    for i in range(0, 10000):
        name_beer = str(get_random_str(10))
        arr_beer.add(name_beer)
        cur.execute('INSERT INTO "Beer"(id_part, id_brewery, name_of_beer, \
                    container, drinkAbility, description, color, strength, volume,\
                    price_purchase, price_selling, price_wholesale, sort) \
                    VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (randint(1, 10000),
            randint(1, 10000),
            name_beer,
            random.choice(beerContainer),
            random.choice(drinkAbility),
            discription,
            random.choice(color),
            random.choice(strength),
            random.choice(volume),
            randint(600, 1000),
            randint(400, 600),
            randint(600, 1000),
            random.choice(arr_sort),
            )
        )

    # SupplyAgreement
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
                random.choice(arr_beer),
                random.choice(beerContainer),
                randint(1, 10000),
                cost,
                '1997-08-24',
                account_number,
                random.choice(arr_account),
                random.choice(arr_institution_name),
                '40:00:00',
                randint(1, 100),
                random.choice([True, False]),
                )
            )

    # Check
    
    # Orders

    # Invoice    
    for i in range(0, 5000):
        cur.execute('INSERT INTO "Invoice"(id_order, id_brewery, id_part, id_agreement, \
                    name_of_beer, container, count, price, data) \
                    VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (randint(1, 10_000),
            randint(1, 10_000)),
            randint(0, 4000),
            randint(0, 10_000),
            random.choice(arr_beer),
            random.choice(beerContainer),
            random.choice(arr_count),
            random.choice(arr_cost),
            '1997-08-24'
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
