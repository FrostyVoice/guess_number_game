import random

name = input("Привет, как тебя зовут? ")
print(f"Чтож, {name}, я загадываю число от 1 до 20.")

number = random.randint(1, 20)
for step in range(1, 6):
    guess = int(input("Попробуй угадать: "))

    if guess < number:
        print("Твое число слишком маленькое.")

    elif guess > number:
        print("Твое число слишком большое.")

    elif guess == number:
        break

if guess == number:
    print(f"Отлично, {name}! Ты справился за {str(step)} попытки!")
else:
    print(f"Увы, я загадал число {str(number)}.")
