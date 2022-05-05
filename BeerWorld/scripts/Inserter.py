from itertools import count
from types import coroutine
from webbrowser import get
import psycopg2
from random import choice
from string import digits
import random
import datetime



def get_random_str(countOfWarehouse): # количество складов 
    universaryCode = []
    for i in range(0, countOfWarehouse):
        str = ''.join(choice(digits) for i in range(10)) 
        universaryCode.append(str)
    return universaryCode

def get_random_int(countOfInt):
    return 1

try:
        
    conn = psycopg2.connect(database="beerWorld",  host="localhost", port=5432)
    conn.autocommit=False
    cur = conn.cursor()

    typeInstitution = ['restaurant', 'bar', 'snack-bar']
    statusInstitution = ['the best', 'middle', 'not so bad']
    trackingOrder = ['inBrewery', 'inWareHouse', 'inInstitution']
    typePayment = ['cash', 'online']

    # warehouse
    countOfWarehouse = 10
    universaryCode = get_random_str(countOfWarehouse)
    address = ['Moscow', 'Volgograd', 'Orenburg', 'Voronezh']
    capacity = [1000, 1500, 2000, 3000, 5000] # Вместимость в литрах
    boss = ['Corey Taylor', 'Sid Wilson', 'Joey Jordison', 
                'Paul Gray', 'Chris Fehn', 'James Root',
                'Craig Jones', ' Mick Thomson'
            ]
    information = ['hihihi']
    coordinaties = [(1,1), ( 1, 3), (4, 5), (1,1)]

    # Institution

    # beer
    beerNames = ['Garage','Essa','Spatten','Miller','Ohota', 'Corona']
    beerContainer = ['bottle', 'barrel', 'tank', 'keg']
    drinkAbility = ['Good', 'Execelent', 'Middle', 'Not so bad']
    discription = 'description'
    color = ['Mash', 'Roasted Malts', 'Fermentation', 'Cold Break']
    strength = [3, 4, 5, 6, 9]
    volume = [1, 5, 10, 100]
    pricePurchase = [10, 12, 15, 17, 20] # за 1 литр
    priceSelling = [20, 24, 30, 34, 40] 
    priceWholeSle = [40, 48, 60, 80]

    country = ['Russia', 'Germany', 'Britain', 'Africa', 'Albany']
    nameOfBrewery = ['Magic Rock Brewing', 'Mikkeller', 'Omnipollo', 'Cloudwater Brew Co',
                     'Lervig Aktiebryggeri', 'Cantillon', 'Brouwerij De Molen',
                     'Magic Rock Brewing', 'Stone Brewing Berlin', 'Beavertown'
                     ]

    # sorts
    sorts = ['Ale', 'Lager', 'Porter', 'Stout', 'Blonde Ale', 'Brown Ales', 'Pale Ale',
            'Wheat', 'Pilsner', 'Sour Ale']

    #Warehouse

    #Create python

    for i in range(0, len(nameOfBrewery)):
        name = nameOfBrewery[i]
        years = random.choice([1700, 1704, 1766, 1800, 1891, 1935, 1983])
        cntry = random.choice(country)

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


   