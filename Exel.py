import pandas as pd
from datetime import datetime

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, '%Y.%m.%d')  # Перетворення рядка в об'єкт дати
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
try:
    data = pd.read_csv('employees.csv')

    data['Вік'] = data['Дата народження'].apply(calculate_age)

    data['№'] = range(1, len(data) + 1)

    data = data[['№', 'Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']]

    with pd.ExcelWriter('exel.xlsx') as writer:
        data.to_excel(writer, sheet_name='all', index=False)

        younger_than_18 = data[data['Вік'] <= 18]
        younger_than_18.to_excel(writer, sheet_name='younger_18', index=False)

        age_18_to_45 = data[(data['Вік'] >= 18) & (data['Вік'] <= 45)]
        age_18_to_45.to_excel(writer, sheet_name='18-45', index=False)

        age_45_to_70 = data[(data['Вік'] > 45) & (data['Вік'] <= 70)]
        age_45_to_70.to_excel(writer, sheet_name='45-70', index=False)

        older_than_70 = data[data['Вік'] > 70]
        older_than_70.to_excel(writer, sheet_name='older_70', index=False)

    print("Ok, програма завершила свою роботу успішно.")
except FileNotFoundError:
    print("Помилка: файл CSV не знайдено.")
except Exception as e:
    print(f"Помилка: {e}. Неможливо створити XLSX файл.")
