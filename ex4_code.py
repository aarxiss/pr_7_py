# Перевірка коректності вводу
while True:
    try:
        num = int(input("Введіть ціле невід’ємне число для обчислення факторіала: "))
        if num < 0:
            print("Число повинно бути не менше 0. Спробуйте ще раз.")
        else:
            break
    except ValueError:
        print("Некоректне введення. Введіть ціле число.")

# Обчислення факторіала з виводом процесу
factorial = 1
i = 1
process = ""

while i <= num:
    factorial *= i
    process += str(i)
    if i != num:
        process += "*"
    i += 1

print(f"{num}! = {process} = {factorial}")
