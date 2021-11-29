for age in range(30):
    n = age % 10
    if n == 1 and age != 11:
        print(age, "Год")
    elif 2 <= n <= 4 and age > 20 or 1 < age < 5:
        print(age, "Года")
    else:
        print(age, "Лет")
