import math
test = 123

bio1 = 'Mam na imię Paweł.'
bio2 = 'Pracuję jako progrmaista Python\'a'

bio = bio1 + '\n' + bio2
print(bio)

login = 'admin'
password = 'haslo1230'

print(f'Login: {login}, password: {password}')

PI = math.pi

print(f'Pole koła o promieniu 2 to: {round(PI * 2 ** 2, 4)}')

height = 1.71
weight = 79. # float
atom_size = 10e-10 # też float


print(atom_size)

a = 13

h = 7

trojkat = (1 / 2) * a * h
print(trojkat)

power_sum = h**2
print(power_sum)

print(round(math.sqrt(3)))

is_adult = False
is_day = True

if is_day:
    print('you can go out')
else:
    if is_adult:
        print('You can go out')
    else:
        print('You can\'t go out. Becouse you are not adult')

is_adult_boy = is_adult and is_day
print(is_adult_boy)


age_a = 'tew'

if age_a > 5:
    print('hohohohoho')
elif age_a <= 5:
    print('heheheheheh')
else:
    print('sodjrhfis')
