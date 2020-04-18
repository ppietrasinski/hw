lb = [1,2,3]
la = list(map(lambda x: str(x), lb))

la.append(4)

print(la)
print(lb)

print('Today is friday')

is_day = True
is_night = False

if is_day:
    print('Sun is shining')
else:
    print('Night sky is dark and full of stars')

'''
Zadanie 1 – If
1. Zdefiniuj zmienną temp_celsius
2. Spraw, żeby dla dla temp_celsius równego 0 wydrukował się napis: “In water freezing point”
3. Dodaj drugą zmienną: pressure_hpa
4. Zmodyfikuj kod z punktu drugiego, aby napis był drukowany przy temp_celsius równego 0 oraz pressure_hpa równego 1013
'''

temp_celcius = 20
pressure_hbpa = 10156

if temp_celcius == 0 and pressure_hbpa == 1013:
    print('In water freezing point')
else:
    print('Not in water freezing point')


'''
Zadanie 2 – If / else
1. Zmodyfikuj kod z zadania pierwszego tak, żeby przy warunkach innych niż temp_celsius równe 0 oraz pressure_hpa równe 1013 drukowany był napis “Not in water freezing point”

Zadanie 3 – elif
    1. Dane są zmienne:
        a. price = 100 (stała cena)
        b. free_product – boolean opisujące darmowy odbiór produktu
        c. cash_amount - ilość gotówki
    2. Zapisz warunek, aby:
        a. Jeśli free_product jest prawdą -> drukowany był napis “You get the product for free!”
        b. Jeśli cash_amount jest równe co najmniej cenie produktu -> drukowany był napis “You can buy this product.”
        c. Jeśli cash_amount jest mniejsze niż cena produktu -> Drukowany był napis: “You need N more cash buy this product.” gdzie N to brakująca do zakupu kwota

'''
price = 100
free_product = False
cash_amount = 19

if free_product:
    print('You get the product for free!')
elif cash_amount >= price:
    print('You can buy this product.')
else:
    print(f'You need {price - cash_amount} more cash buy this product.')



'''

Zadanie 4 - pętla for range()
    Wydrukuj trzecie potęgi liczb naturalnych od 11 do 27

Zadanie 5 - pętla for dla listy
    Mając daną listę liczb: numbers = [3, 12, 55, 178, 1300, 6789, 19200] wydrukuj Każdą z tych liczb pomnożoną przez 3

Zadanie 6 - pętla for + if
    Dla listy z zadania 5 wydrukuj wszystkie liczby podzielne przez 3'''