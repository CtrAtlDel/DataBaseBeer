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
    cursor = conn.cursor()

    cursor.execute('SELECT id_order FROM "Orders"')
    id_order = [id[0] for id in cursor.fetchall()]

    cursor.execute('SELECT id_brewery FROM "Brewery"')
    id_brewery = [id[0] for id in cursor.fetchall()]

    cursor.execute('SELECT id_part FROM "Part"')
    id_part = [id[0] for id in cursor.fetchall()]

    cursor.execute('SELECT id_agreement FROM "SupplyAgreement"')
    id_agreement = [id[0] for id in cursor.fetchall()]

    cursor.execute('SELECT name_of_beer FROM "Beer"')
    name_of_beer = [name[0] for name in cursor.fetchall()]



    # Ivoice
    for i in range(0, 10_000):
        cursor.execute('INSERT INTO "Invoice"(id_order, id_brewery, \
        id_part, id_agreement, name_of_beer, container, count, price, data) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            [
                random.choice(id_order),
                random.choice(id_brewery),
                random.choice(id_part),
                random.choice(id_agreement),
                random.choice(name_of_beer),
                random.choice(beerContainer),
                randint(3, 1000),
                randint(3, 1049),
                '1997-08-24'
            ])
    

except (Exception, psycopg2.DatabaseError) as error :
    print ("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
    conn.rollback()
finally:
    conn.commit()
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")