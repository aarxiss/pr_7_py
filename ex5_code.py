# Початкові значення
start_population = 10

# Отримання максимальної кількості від користувача
while True:
    try:
        max_population = int(input("Введіть максимальну кількість бактерій: "))
        if max_population <= start_population:
            print(f"Максимум має бути більшим за {start_population}. Спробуйте ще раз.")
        else:
            break
    except ValueError:
        print("Будь ласка, введіть ціле число.")

growth_rate = 20  # у відсотках
hours = 0
population = start_population

# Симуляція росту
print("\nГодина | Кількість бактерій")
print("---------------------------")

while population < max_population:
    print(f"{hours:>6} | {int(population)}")
    population += population * (growth_rate / 100)
    hours += 1

# Останній стан
print(f"{hours:>6} | {int(population)}")
print(f"\nДля досягнення популяції понад {max_population} знадобилось {hours} годин.")
