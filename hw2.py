'''Zadanie 1
Używając podanych zmiennych:
Wydrukuj dokładnie tak sformatowany tekst:
My name is James Michaels. I'm 44 years old. You can contact me via email: jmicheals@example.com or phone: 12343214433.
'''

first_name = 'James'
last_name = 'Micheals'
email = 'jmichaels@example.com'
phone = '12343214433'
age = 44

print(f'My name is {first_name, last_name}. I\'m {age} years old. You can contact me via email: {email} or phone: {phone}')
'''
Zadanie 2
Zdefiniuj dwie zmienne (użyjesz ich poniżej):
· pi - zawierającą wartość liczby pi z dokładnością do czwartego miejsca po przecinku
· r - zawierającą promien koła o wartości 20
Przypisz do nowych zmiennych:
· circumference - obwód koła o promieniu r
· area – pole koła o promieniu r
'''
import math
pi = round(math.pi, 4)
r = 20

circumference = pi * (r**2)
area = 2 * pi * r

print(circumference)
print(area)

'''
Zadanie 3
Używając twierdzenia Pitagorasa oblicz długość przeciwprostokątnej trójkąta
prostokątnego z bokami przy kącie prostym o wartościach:
· a = 5
· b = 13
Wynik wydrukuj z zaokrągleniem do dwóch miejsc po przecinku. Policz i wydrukuj
pole i obwód tego trójkąta.
'''

a = 5
b = 13

c = math.sqrt(a**2 + b**2)
print(round(c, 2))

'''
Zadanie 4
W pewnym sklepie wprowadzono promocję, z której skorzystać mogą osoby
spełniające jeden z następujących warunków:
1. Wszystkie osoby powyżej 65 roku życia
2. Kobiety do 16 roku życia lub po 45 roku życia
3. Mężczyźni od 20 do 40 roku życia

Policz wartość zmiennej typu boolean can_use_promotion opisującą czy dana osoba może skorzystać z promocji dla następujących osób:
· Marta, studentka w wieku 22 lat
· Pan Marian, emeryt w wieku 72 lata
· Pani Ewa, 46 letnia księgowa
· Tomek, uczen w wieku 12 lat
· Janusz, kierowca Passata w kwiecie wieku (40 lat)
'''

Marta_sex = 'female'
Marta_age = 22
#false

Marian_sex = 'male'
Marian_age = 72
#True

Ewa_sex = 'female'
Ewa_age = 46
#True

Tomek_sex = 'male'
Tomek_age = 12
#True

Janusz_sex = 'male'
Janusz_age = 41
#false

sex = Janusz_sex
age = Janusz_age

can_use_promotion = 65 <= age or (sex == 'female' and (age <= 16 or 45 <= age)) or (sex == 'male' and (20 <= age <= 40))
print(can_use_promotion)

# x = {'a', 'b', 'c', 'd'}
# y = {'c', 'e', 'f'}
# z = {'a', 'g', 'h', 'i'}
#
# # What is the value of x | y ^ z?
# # y ^ z -> suma zbiorów -> wszystkie elementy które znajdują się w zbiorze bez powtarzania się
# '''
# np:
# y = {'c', 'e', 'f', 'i'}        z = {'a', 'g', 'h', 'i'}
# y ^ z = {'e', 'g', 'c', 'f', 'h', 'a'}
#
# y = {'c', 'e', 'f'}        z = {'a', 'g', 'h', 'i'}
# y ^ z = {'f', 'i', 'e', 'g', 'c', 'h', 'a'}
# '''
#
# # y | z -> iloczyn zbiorów -> wszystkie elementy wspólne obu zbiorów
# '''
# np:
# y = {'c', 'e', 'f', 'i'}        z = {'a', 'g', 'h', 'i'}
# y | z = {'e', 'g', 'c', 'f', 'h', 'a'}
#
# y = {'c', 'e', 'f'}        z = {'a', 'g', 'h', 'i'}
# y ^ z = {'f', 'i', 'e', 'g', 'c', 'h', 'a'}
#
# s.union(t)                  s | t       new set with elements from both s and t                 nowy set ze wszystkimi elementami zbiorów s i t -> elementy powtarzająće się sa zapisywane raz
# s.symmetric_difference(t)   s ^ t       new set with elements in either s or t but not both     nowy set z elementami ze zbiorów s oraz t bez tych które się powtarzają
# '''
# a = {'a', 'b', 'c'}
# b = {'c', 'd', 'e'}
#
# print(a ^ b)