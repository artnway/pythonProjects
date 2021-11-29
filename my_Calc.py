import time
while True:
    print ("\nПупсява-мурсява призвала меня посчитать ей циферки")
    time.sleep(.5)
    a = str(input("\nВыберите операцию(+.-,/,*): "))
    b = int(input("Введите первое число: "))
    c = int(input("Введите второе число: "))
    q = 'Результа = '
    if a == '+':
        x = b+c
        print(q+str(x))
    elif a == '-':
        x = b-c
        print(q+str(x))
    elif a == '/':
        x = b/c
        print(q+str(x))
    elif a == '*':
        x = b*c
        print(q+str(x))
    else:
        print("Выбрана неверная операция")
    w = input("Начать заново? y/n ")
    if w == 'n':
        break



