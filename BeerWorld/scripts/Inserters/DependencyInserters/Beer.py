from locale import currency
import psycopg2
from random import choice, randint
import string    
import random 

strength = [3, 4, 5, 6, 9]
volume = [1, 5, 10, 100]

arr_institution_name = []
arr_sort = []
arr_beer = []
arr_account = []
arr_cost = []
arr_count = []
arr_beer = []


def get_random_str(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))  


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

    cur.execute('SELECT id_part FROM "Part"')
    id_part = [id[0] for id in cur.fetchall()]

    cur.execute('SELECT id_brewery FROM "Brewery"')
    id_brewery = [id[0] for id in  cur.fetchall()]

    for i in range(0, 10_000):
        name_beer = str(get_random_str(10))
        arr_beer.append(name_beer)
        cur.execute('INSERT INTO "Beer"(id_part, id_brewery, name_of_beer, \
                    container, drinkAbility, description, color, strength, volume,\
                    price_purchase, price_selling, price_wholesale, sort) \
                    VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (random.choice(id_part),
            random.choice(id_part),
            str(get_random_str(10)),
            random.choice(beerContainer),
            random.choice(drinkAbility),
            discription,
            random.choice(color),
            random.choice(strength),
            random.choice(volume),
            randint(600, 1000),
            randint(400, 600),
            randint(800, 1000),
            str(get_random_str(10)),
            )
        )

    
    # # SupplyAgreement
       
    # for i in range(0, 10000):
    #     account_number = get_random_str(20)
    #     cost = randint(1, 5000)
    #     arr_cost.append(cost)
    #     arr_count = randint(1, 5000)
    #     arr_account.append(account_number)
    #     cur.execute('INSERT INTO "SupplyAgreement"(id_institution, name_beer, \
    #                     container, count_of_beer, cost, start_date, account_number, \
    #                     prepayment, name_of_institution, delivery_period, count_of_delivery, isImporter) \
    #                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
    #         (randint(1, 10000),
    #         random.choice(arr_beer),
    #         random.choice(beerContainer),
    #         randint(1, 10000),
    #         cost,
    #         '1997-08-24',
    #         account_number,
    #         random.choice(arr_account),
    #         random.choice(arr_institution_name),
    #         '40:00:00',
    #         randint(1, 100),
    #         random.choice([True, False]),
    #         )
    #     )

    # # Check
    
    # # Orders

    # # Invoice    
    # for i in range(0, 5000):
    #     cur.execute('INSERT INTO "Invoice"(id_order, id_brewery, id_part, id_agreement, \
    #                 name_of_beer, container, count, price, data) \
    #                 VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
    #         (randint(1, 10_000),
    #         randint(1, 10_000),
    #         randint(0, 4000),
    #         randint(0, 10_000),
    #         random.choice(arr_beer),
    #         random.choice(beerContainer),
    #         random.choice(arr_count),
    #         random.choice(arr_cost),
    #         '1997-08-24')
    #     )
    
    
    

except (Exception, psycopg2.DatabaseError) as error :
    print ("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
    conn.rollback()
finally:
    conn.commit()
    if conn:
        cur.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")