what = input ("Что делаем? (+, -): ")

a = input("Введи первое число: ")
b = input("Введи второе число: ")

if what == "+":
    c = a + b
    print ("Результат: " + c )
elif what == "-":
    c = a - b
    print ("Результат: " + c )
else:
    print("Выбрана неверная операция!")