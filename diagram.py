import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

try:
    data = pd.read_csv('employees.csv')
    print("Ok: Файл CSV успішно завантажено.")
except FileNotFoundError:
    print("Помилка: Файл CSV не знайдено.")
    exit(1)
except Exception as e:
    print(f"Помилка: {e}. Неможливо відкрити файл CSV.")
    exit(1)

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, '%Y.%m.%d')  # Перетворення рядка в об'єкт дати
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

data['Вік'] = data['Дата народження'].apply(calculate_age)

gender_counts = data['Стать'].value_counts()

print("\nКількість співробітників чоловічої і жіночої статі:")
print(gender_counts)

plt.figure(figsize=(8, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values)
plt.title("Розподіл співробітників за статтю")
plt.xlabel("Стать")
plt.ylabel("Кількість")
plt.show()

bins = [0, 18, 45, 70, 80]  
age_labels = ["до 18", "18-45", "45-70", "старше 70"]  

data['Вікова категорія'] = pd.cut(data['Вік'], bins=bins, labels=age_labels)

age_category_counts = data['Вікова категорія'].value_counts()

print("\nКількість співробітників в різних вікових категоріях:")
print(age_category_counts)

plt.figure(figsize=(8, 6))
sns.barplot(x=age_category_counts.index, y=age_category_counts.values)
plt.title("Розподіл співробітників за віковими категоріями")
plt.xlabel("Вікова категорія")
plt.ylabel("Кількість")
plt.show()

gender_age_counts = data.groupby(['Вікова категорія', 'Стать']).size().unstack(fill_value=0)

print("\nКількість співробітників чоловічої та жіночої статі в різних вікових категоріях:")
print(gender_age_counts)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
colors = ['lightblue', 'lightcoral']

for i, age_category in enumerate(age_labels):
    ax = axes[i // 2, i % 2]
    ax.pie(gender_age_counts.loc[age_category], labels=gender_age_counts.columns, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85)
    ax.set_title(f"Вікова категорія: {age_category}")

plt.tight_layout()
plt.show()