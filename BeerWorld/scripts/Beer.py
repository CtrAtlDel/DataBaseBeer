from Inserter import get_random_int, get_random_str
from Slicer import getBreweryAndBeerName, getBreweryes

# beer
beerNames = ['Garage',
    'Essa',
    'Spatten',
    'Miller',
    'Ohota',
    'Corona',
    '']
    
beerContainer = ['bottle', 'barrel', 'tank', 'keg']
drinkAbility = ['Good', 'Execelent', 'Middle', 'Not so bad']
discription = 'description'
color = ['Mash', 'Roasted Malts', 'Fermentation', 'Cold Break']
strength = [3, 4, 5, 6, 9]
volume = [1, 5, 10, 100]
pricePurchase = [10, 12, 15, 17, 20] # за 1 литр
priceSelling = [20, 24, 30, 34, 40] 
priceWholeSle = [40, 48, 60, 80]

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
country = ['Russia', 'Germany', 'Britain', 'Africa', 'Albany', 'USA',
            'Abkhazia', 'Australia', 'Armenia', 'Bahamas', 'Bulgaria', 'Haiti',
            'Haiti', 'Guatemala', 'Germany', 'Greenland', 'Greece', 'Denmark',
            'Egypt', 'Israel', 'Jordan', 'Ireland', 'Spain', 'Italy']

nameOfBrewery = getBreweryes()

brew = getBreweryAndBeerName()

# sorts
sorts = ['Ale', 'Lager', 'Porter', 'Stout', 'Blonde Ale', 'Brown Ales', 'Pale Ale',
        'Wheat', 'Pilsner', 'Sour Ale', 'Russian', 'zxc', 'IPA']

#Warehouse

#Create python
