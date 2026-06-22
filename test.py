# stolica = dict(
#     polska = 'Warszawa',
#     Włochy = 'Rzym',
#     Francja = 'Paryż'
# )
# stolica['hiszpania'] = 'madryt'
#
# nowe_klucze = [i.capitalize() for i in stolica.keys()]
# nowe_values = [i.capitalize() for i in stolica.values()]
#
# stolice = dict(zip(nowe_klucze, nowe_values))
#
# haslo = (input('podaj panstwo: ').capitalize())
#
# # del stolice['Francja']
#
# if stolice.get(haslo) == None:
#     print("stolica nie zostala wprowadzona do bazy danych")
# else:
#     print(f'stolica {haslo} to', stolice.get(haslo))
from pandas.conftest import index

# a = {1,2,3,4,5,6,7,8,9,10}
# b = {"s","a","P"}
#
# print(a|b)

# liczby = [1, 2, 3, 4, 5]
# liczby.extend("6")
# liczby = [int(i) for i in liczby]
# print(liczby)


# mieszane = [1, 2.5, "tekst"]
# szukana_wartosc = 1
#
# if szukana_wartosc in mieszane:
#     print(f'{szukana_wartosc} znajduej sie na liscie')
# else:
#     print("nie ma na lisie")

#
# uczen = {"imie": "Ala", "oceny": [5, 4, 3]}
#
# # for i in uczen["oceny"]:
# #     print(i, end =" ")
# print(*uczen["oceny"])


# liczby = [1, 2, 3, 4, 5]
# print(*liczby)
#
# haslo = input('podaj haslo : ')
#
# while True:
#     if haslo == "Moninski":
#         print("podane haslo jest poprawne")
#         break
#     else:
#         haslo = input('podaj haslo : ')


# rects = [
#     (10, 50),
#     (10, 9),
#     (15, 3),
#     (30, 45)
# ]
#
# for a, b in rects:
#     print(a * b)


# slowa = ["kot", "hipopotam", "pies"]
#
# """
# ta funkcja pokazuje dochstring
#
# """
#
# print(sorted(slowa, key = lambda x: (len(x))))




# def wypisz_powitanie(imie, nierormalne = False):
#     if nierormalne == True:
#         return f'Siemasz {imie}'
#     else:
#         return f'Milo Cie widziec {imie}'
#
# print(wypisz_powitanie("moninski",nierormalne = True))

# V=1/3*3.14*r(2)*h
# stozki = [
#     (10, 5),
#     (15, 5),
#     (5, 10),
#     (5, 15)
# ]
#
# for r,h in stozki:
#    print((1/3)*3.14*(r**2)*h)

# zakresy = [range(0, 10), range(0, 150), range(30, 50)]
#
# liczba = int(input('podaj liczbe: '))
#
# for i in zakresy:
#     if liczba in i:
#         print('tak')
#     else:
#         print('nie')

# bardzo_dobry = list(range(90,101))
# dobry+ = list(range(81,90))
# dobry = list(range(71,80))
# dostateczny+ = list(range(61,70))
# dostateczny = list(range(51,60))
# niedostateczny = list(range(0,50))


lista_a = [23, 45, 67, 67, "qw", "er", "ty", "qw"]
lista_b = [23, 23, 45, 67, "qw", "er", "ty"]
lista_c = [23, 45, 67, "qw", "er", "ty"]


def all_unique(a):
    if len(a) == len(set(a)):
        return True
    else:
        return False

print(all_unique(lista_a))


