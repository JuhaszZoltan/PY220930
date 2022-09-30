# egész szám
a:int = 10

print(10 + 2)

print(10 / 3) # 'sima' osztás
print(10 // 3) # egész osztás
print(10 % 3) # maradékszámítás

print(2 ** 10) # hatványozás

# lebegőpontos szám
b:float = 3.14

print(2 ** 0.5)
print(20 + 2.123)

# karakterlánc (string)
c:str = 'cica'
e:str = "kutya"

print("Feri azt mondta: Don't give up!")
print('Feri azt mondja: "Ne add fel!"')
# konkatenáció (összefűzés)
print('Feri azt mondta: "Don' + "'" + 't give up!"')
# sorozatos összefűzés
print('cica ' * 10)

# logikai (boolean)
d:bool = True # vagy False

print(True and False) # 'és'
print(True or False) # 'vagy'
print(not True) # tagadás

# összahasonlító (compare) operátorok:
# <, >, <=, <=, ==, !=

# halmazműveletek:
print('A' in {'A', 'B', 'C'}) # 'eleme' / 'tartalmazza'
print(11 not in [6, 5, 5, 11, 3, 20]) # 'nem eleme', 'nem tartalmazza'

# összetett adatszerkezetek:

# halmaz:
halmaz:set[int] = { 5, 2, 88, 4, 12, 1 }
print(halmaz)

# lista:
lista:list[str] = ['kalap', 'nyakkendő', 'póló', 'póló', 'kabát']
print(lista)

# a különbség:
# halmazon NEM értelmezezz a sorrend, istán IGEN
# halmazban NEM LEHET ismétlődés, listában LEHET