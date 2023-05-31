print("I will now count my chickens:")
#Использует оператор + для сложения и оператор / для деления. Учитывая последовательность выполнения - сначала деление потом сложение
print("Hens", 25 + 30 / 6) 
# Оператор % используется для вывода остатка от деления 75 на 4. У умножения и остатка от деления одинаковый приоритет выполнения
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")
#Сначала высчитывается 4%2(остаток от деления) дальше -1/4 
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7?")
#True это истина False ложь. Если 3 + 2 < 5 - 7 оказывается верным значит True, в обратном случае False. В данном случае False
print(3 + 2 < 5 - 7)
#Просто сложение 3+2. Те цифры что указаны в строке считаются за строку а не int. Так что результат 5
print("What is 3 + 2?", 3 + 2)
#Вычитание
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")
#Если выражение истина, то True. В данном случае True
print("Is it greater?", 5 > -2)
#В этом случае если 5 больше или равно -2. Выдаст True
print("Is it greater or equal?", 5 >= -2)
#Пять Меньше или равно -2. Выдаст False
print("Is it less or equal?", 5 <= -2)
#3. Придумайте вычисление посложнее и создайте новый файл .ру, который выполнит его. Факториал числа 9
factorial_result = 1
number = 9
for i in range(1, number + 1):
    factorial_result *= i
print(f"Факториал числа {number} равен {factorial_result}")
#5. Перепишите код из примера ехз.ру, используя числа с плавающей
#точкой, чтобы произвести более точные вычисления (подсказка:
#20.0 — число с плавающей точкой).
print("I will now count my chickens:")

print("Hens", 25.0 + 30.0 / 6.0)
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")

print(3.0 + 2.0 < 5.0 - 7.0)

print("What is 3 + 2?", 3.0 + 2.0)
print("What is 5 - 7?", 5.0 - 7.0)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)



