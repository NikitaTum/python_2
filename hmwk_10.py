# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите кол-во монет: "))
count_a = 0
count_b = 0
for i in range(n):
    a = int(input())
    if a == 0:
        count_a += 1
    else:
        count_b += 1
if count_b > count_a:
    print(count_a)
else:
    print(count_b)