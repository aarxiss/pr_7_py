# Запитуємо початкові дані
initial_amount = float(input("Введіть початкову суму вкладу (грн): "))
interest_rate = float(input("Введіть річну процентну ставку (%): "))
target_amount = float(input("Введіть бажану кінцеву суму (грн): "))

# Ініціалізуємо поточну суму та кількість років
current_amount = initial_amount
years = 0

# Обчислення накопичення за допомогою циклу while
while current_amount < target_amount:
    years += 1
    current_amount += current_amount * (interest_rate / 100)
    print(f"Рік {years}: {current_amount:.2f} грн")

# Вивід фінального результату
print(f"\nЩоб накопичити {target_amount:.2f} грн, знадобиться {years} років.")
