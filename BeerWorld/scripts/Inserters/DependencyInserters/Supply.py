
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
    
    # SupplyAgreement
    
    cursor.execute('SELECT id_beer FROM "Beer"')
    id_beer = [id[0] for id in cursor.fetchall()]



    cursor.execute('SELECT name_of_beer FROM "Beer"')
    name_of_beer = [id[0] for id in cursor.fetchall()]

    cursor.execute('SELECT id_institution FROM "Institution"')
    id_instituition = [id[0] for id in cursor.fetchall()]

    cursor.execute('SELECT name FROM "Institution"')
    name_instituition = [id[0] for id in cursor.fetchall()]   

    cursor.execute('SELECT id_institution FROM "Institution"')
    id_institution = [id[0] for id in cursor.fetchall()]

    #SupplyAgreement
    for i in range(0, 10_000):
        account_number = get_random_str(20)
        cost = randint(1, 5000)
        cursor.execute('INSERT INTO "SupplyAgreement"(id_institution, name_beer, \
                        container, count_of_beer, cost, start_date, account_number, \
                        prepayment, name_of_institution, delivery_period, count_of_delivery, isImporter) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (random.choice(id_instituition),
            random.choice(name_of_beer),
            random.choice(beerContainer),
            randint(1, 10_000),
            randint(1, 5000),
            '1997-08-24',
            account_number,
            randint(1, 100),
            random.choice(name_instituition),
            '40:00:00',
            randint(1, 100),
            random.choice([True, False])
            )
        )

except (Exception, psycopg2.DatabaseError) as error :
    print ("Ошибка в транзакции. Отмена всех остальных операций транзакции", error)
    conn.rollback()
finally:
    conn.commit()
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")