import random
import datetime

female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
surnames = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
countries = ['Poland', 'United Kingdom', 'Germany', 'France', 'Other']

current_year = datetime.datetime.now().strftime('%Y')
users_list = []

for i in range(10):
    if i <= 5:
        name = random.choice(female_fnames)
    else:
        name = random.choice(male_fnames)
    lastname = random.choice(surnames)
    email = f'{name}.{lastname}@example.com'
    age = random.randint(5, 45)
    country = random.choice(countries)
    adult = True if age >= 18 else False

    user_dict = {
        'firstname': name,
        'lastname': lastname,
        'email': email,
        'age': age,
        'country': country,
        'adult': adult
    }
    users_list.append(user_dict)

# print(type(current_year))

for user in users_list:
    print(f"Hi! I'm {user['firstname']} {user['lastname']}. "
          f"I come from {user['country']} and I was born "
          f"in {int(current_year) - user['age']}")


