import random

# Генеруємо випадкове число від 1 до 100
secret_number = random.randint(1, 100)
attempts = 7

print("Вгадай число від 1 до 100. У тебе є 7 спроб!")

for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Спроба {attempt}: Введи число: "))
    except ValueError:
        print("Будь ласка, введи коректне ціле число.")
        continue

    if guess < secret_number:
        print("Загадане число більше.")
    elif guess > secret_number:
        print("Загадане число менше.")
    else:
        print(f"Вітаю! Ти вгадав число за {attempt} спроб(у/и)!")
        break
else:
    print(f"На жаль, ти не вгадав. Загадане число було: {secret_number}")
