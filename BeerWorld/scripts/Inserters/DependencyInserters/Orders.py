from numpy import ALLOW_THREADS
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
trackingOrder = ['inBrewery', 'inWareHouse', 'inInstitution'] # TODO trackeing
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

    cursor.execute('SELECT id_brewery FROM "Brewery"')
    id_brewery = [id[0] for id in cursor.fetchall()]

    cursor.execute('SELECT id_part FROM "Part"')
    id_part = [id[0] for id in cursor.fetchall()]

    cursor.execute('SELECT id_agreement FROM "SupplyAgreement"')
    id_agreement = [id[0] for id in cursor.fetchall()]


    for i in range(0, 10_000):

        all_sum = randint(1, 5000)
        all_count = randint(1, 5000)
        all_half = randint(5, 5000)
        half = randint(1, all_half - 1)
        tracking = random.choice(trackingOrder)
        ishalfpayed = random.choice([True, False])
        isallpayed = random.choice([True, False])

        cursor.execute('INSERT INTO "Orders"(agreement_id, all_sum, all_count, half, \
            all_half, tracking, isHalfPayed, isAllPayed) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', 
            [
                random.choice(id_agreement),
                all_sum,
                all_count,
                half,
                all_half,
                tracking,
                ishalfpayed,
                isallpayed
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