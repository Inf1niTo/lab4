#NUM 1
values = []
line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
while line != 0:
    num = float(line)
    values.append(num)
    line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
values.sort()
print(values)
