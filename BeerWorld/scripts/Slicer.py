from ast import Break
from distutils.command.build_scripts import first_line_re
import re


def BreweryAndBeerName():
    brewery = "(МПК) Московская Пивоваренная Компания, («Жигули», «Хамовники», «Моспиво», «Oettinger», «Faxe») Балтика, (" \
            "«Балтика», «Невское», «Ярпиво», «Туборг», «Карлсберг», «Kronenbourg 1664 Blanc»)Жигулёвский пивоваренный " \
            "завод ,(«Жигулевское», «Самарское», «Фон Вакано», «Старая Самара») SUN InBev Russia ,(«BUD», «Клинское», " \
            "«Сибирская Корона», «Staropramen»)Efes Russia ,(«Золотая Бочка Классическое», «Efes Pilsener» " \
            "«Velkopopovicky Kozel») HEINEKEN Russia ,(«Бочкарев», «Три медведя», «Guinness Original») Волковская " \
            "Пивоварня ,(«Волчок», «Светлячок», «APA», «IPA», «Порт Артур») Вятич ,(«Вятич», «Жигулевское», «Бочковое», " \
            "«Пшеничное», «Жигулевское Экспорт») Завод Трёхсосенский ,(«Трёхсосенское», «Искусство варить», " \
            "«Дуб и Обруч», «Жигулёвское») Афанасий ,(«Афанасий», «Марочное», «Живое пиво», «Домашнее», " \
            "«ЭкоBeer»)Очаково ,(«Altstein», «Очаково», «Ячменный колос», «Жигулевское»), Mikkeller, Omnipollo, Cloudwater Brew Co," \
            "Lervig Aktiebryggeri, Cantillon, Brouwerij De Molen," \
            "Magic Rock Brewing, 'Stone Brewing Berlin, Beavertown "

    brewerys = list(map(str.strip, re.sub(r'\([^()]*\)', '', brewery).split(","))) 

    print(brewerys)
    

print(BreweryAndBeerName())
    

