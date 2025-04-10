# Введення меж діапазону
try:
    lower = int(input("Введіть нижню межу діапазону: "))
    upper = int(input("Введіть верхню межу діапазону: "))
except ValueError:
    print("Будь ласка, введіть коректні цілі числа.")
    exit()

# Перевірка та пошук простих чисел
prime_numbers = []

for num in range(lower, upper + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # перевірка до кореня числа
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

# Виведення результату
if prime_numbers:
    print("Прості числа у вказаному діапазоні:")
    print(prime_numbers)
else:
    print("У вказаному діапазоні немає простих чисел.")
