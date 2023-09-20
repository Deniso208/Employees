import csv
import random
from faker import Faker
from full_names import ukrainian_middle_names


fake = Faker('uk_UA')

with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()

    for i in range(1, 20000):
        gender = random.choice(['Чоловік', 'Жінка'])
        birthdate = fake.date_of_birth(minimum_age=16, maximum_age=72)
        # Вираховуємо, щоб 40% жінок і 60% чоловіків
        if (i % 10) < 4:  # 4 з 10 - це 40%
            gender = 'Жінка'
            full_name = fake.first_name_female(), fake.last_name_female()
        else:
            gender = 'Чоловік'
            full_name = fake.first_name_male(), fake.last_name_male()
        
        # Вибираємо випадковий по батькові зі списку
        middle_name = random.choice(ukrainian_middle_names)

        writer.writerow({
            'Прізвище': full_name[1],
            'Ім’я': full_name[0],
            'По батькові': middle_name,  # Використовуємо тут випадковий по батькові
            'Стать': gender,
            'Дата народження': birthdate.strftime('%Y.%m.%d'),
            'Посада': fake.job(),
            'Місто проживання': fake.city(),
            'Адреса проживання': fake.address(),
            'Телефон': fake.phone_number(),
            'Email': fake.email()
        })

print("Готово! Таблиця була збережена у файлі 'employees.csv' з кодировкою UTF-8 і номерами рядків.")
