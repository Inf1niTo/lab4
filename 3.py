#NUM 3
values = []
line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
while line != 0:
    num = float(line)
    values.append(num)
    line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
values.sort()
print("Начальный список:\n", values)
values.pop(0)
values.pop(-1)
print("Обновленный список:\n", values)