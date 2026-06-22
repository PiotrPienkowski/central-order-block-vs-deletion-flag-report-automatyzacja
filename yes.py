# lista_a = [23, 45, 67, 67, "qw", "er", "ty", "qw"]
# lista_b = [23, 23, 45, 67, "qw", "er", "ty"]
# lista_c = [23, 45, 67, "qw", "er", "ty"]
#
# def all_unique(a):
#     if len(a) == len(set(a)):
#         return True
#     else:
#         return False
#
# print(all_unique(lista_c))



# def cenzura(slowo) -> str:
#     return len(slowo) * "*"
#
# print(cenzura('as'))


#
# def na_slowa(zdanie) -> str:
#     return zdanie.split()
#
# print(na_slowa("moninski to jest glupi arschloch"))


# def wielkie_slowa(zdanie) -> str:
#     return [i.capitalize() for i in zdanie.split() if i not in [".", ",", "!", "?"]]
#
#
# print(wielkie_slowa('moninski ! style'))



# tekst = "Image not loading in python raspbian."
# slowa = ["CONVERT", "A", "TUPLE", "TO", "A", "LIST"]
#
#
# def dodaj_slowa(slowa,tekst):
#     slowa.extend(tekst.split())
#     return slowa
#
# print(dodaj_slowa(slowa,tekst))

# def dodaj_slowa(tekst,slowa):
#     for i in tekst.split():
#         slowa.append(i)
#     return slowa
# print(dodaj_slowa(tekst,slowa))


def preprocessing(liczby: list) -> list:
    return [i for i in liczby]

print(preprocessing("abc"))