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

    # Check
    cursor.execute('SELECT distinct account_number FROM "SupplyAgreement"')
    account_number = [id[0] for id in cursor.fetchall()]

    cursor.execute('SELECT distinct id_agreement FROM "SupplyAgreement"')
    id_agreement = [id[0] for id in cursor.fetchall()]

    for i in range(0, 10_000):
        cursor.execute('INSERT INTO "Check" (id_agreement, account_number, \
        sum) \
        VALUES (%s, %s, %s)',
            [random.choice(id_agreement),
            random.choice(account_number),
            randint(1, 5000)
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