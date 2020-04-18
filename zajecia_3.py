a, b, c = 12.4, 3, -50

print(abs(min(a, b, c)))

# first_name = 'pawel'
# print(first_name.capitalize())

name, company = 'ricardo', 'fbi'

print(f"Officer {name.capitalize()} works for {company.upper()}")

# LISTY

friends = ['Pawel', 'Magdzia', 'Wojtek', 'Tomek']

print(friends[0])
print(friends[2])
print(friends[-1])

print('\nZADANIE 3\n')

'''
3. Wykonaj poniższe:
    a. Stwórz listę swoich 5 ulubionych filmów
    b. Wydrukuj długość listy
    c. Wydrukuj 3 element tej listy
    d. Dodaj na koniec listy element “Joker”
    e. Wydrukuj ostatni element na liście
    f. Wydrukuj dwa pierwsze elementy listy
'''

films = ['Batman', 'Matrix', 'Terminator', 'Troy', 'Lion King']

# print(len(films))
# print(films[:3])
# print(films[-1])
# films.append('Joker')
# print(films[-1])
# print(*films[:2])


# DICTs

print('\nZADANIE 4\n')

friend ={
    'email': 'test@test.pl',
    'name': 'Pawel',
    'username': 'Pafcio',
    'lastname': 'Testowy'
}

print(friend)

friend['company'] = 'unemployed'

print(friend)

italy = {
    'country_name': 'Italy',
    'language': 'Italian',
    'population': 60_360_000,
    'capital': 'Rome',
    'famous_people': ['Roberto Benigni', 'Leonardo da Vinci']
}

poland = {
    'country_name': 'Poland',
    'language': 'Polish',
    'population': 38_000_000,
    'capital': 'Warsaw',
    'famous_people': ['John Paul II', 'Robert Lewandowski']
}

france = {
    'country_name': 'France',
    'language': 'French',
    'population': 65_000_000,
    'capital': 'Paris',
    'famous_people': ['Charles de Gaul', 'Zinedine Zidane', 'Napoleon Bonaparte']
}

countries = [italy, france, poland]

print(countries[-1]['capital'])
print(countries[0]['population'])

