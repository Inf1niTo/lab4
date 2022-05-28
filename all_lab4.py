#NUM 1
# values = []
# line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
# while line != 0:
#     num = float(line)
#     values.append(num)
#     line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
# values.sort()
# print(values)

#NUM 2
# values = []
# line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
# while line != 0:
#     num = float(line)
#     values.append(num)
#     line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
# values.sort(reverse=True)
# print(values)

#NUM 3
# values = []
# line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
# while line != 0:
#     num = float(line)
#     values.append(num)
#     line = int(input("Введите число для добавления в список. Для окончания ввода, введите 0\n"))
# values.sort()
# print("Начальный список:\n", values)
# values.pop(0)
# values.pop(-1)
# print("Обновленный список:\n", values)

#NUM 4
# words = []
# n_words = []
# line = str(input("Введите слово для добавления в список. Для окончания ввода, нажмите Enter\n"))
# while line != '':
#     slovo = str(line)
#     words.append(slovo)
#     line = str(input("Введите слово для добавления в список. Для окончания ввода,нажмите Enter\n"))
# for w in words:
#     if w not in n_words:
#         n_words.append(w)
# print("Старый список:\n", words, '\n', "Новый список:\n", n_words)

#NUM 5
# chisla = []
# m_chisla = []
# n_chisla = []
# p_chisla = []
# line = int(input("Введите число для добавления в список. Для окончания ввода, введите 00\n"))
# try:
#     while list != '':
#         if line < 0:
#             minus = int(line)
#             m_chisla.append(minus)
#             line = int(input("Введите число для добавления в список. Для окончания ввода,нажмите Enter\n"))
#         elif line == 0:
#             null = int(line)
#             n_chisla.append(null)
#             line = int(input("Введите число для добавления в список. Для окончания ввода,нажмите Enter\n"))
#         elif line > 0:
#             plus = int(line)
#             p_chisla.append(plus)
#             line = int(input("Введите число для добавления в список. Для окончания ввода, нажмите Enter\n"))
# except ValueError:
#     list == ''
# print(m_chisla, n_chisla, p_chisla)

#NUM 6
# chisla = []
# for i in range(1, 10000):
#     s = 0
#     for j in range(1, int(i // 2) + 1):
#         if i % j == 0:
#             s += j
#     if s == i:
#         num = int(i)
#         chisla.append(num)
# print(chisla)

#NUM 7
# a = 0
# k = 0
# b = 0
# chisla = []
# m_chisla = []
# n_chisla = []
# b_chisla = []
# while b != '':
#     n = int(input("Введите число.\n"))
#     chislo = int(n)
#     chisla.append(chislo)
#     a += n
#     k += 1
#     b = input("Если хотите закончить, нажмите Enter. Если нет, введите любой символ\n")
# s = a / k
# for i in range(0, k):
#     if chisla[i] < s:
#         min = int(chisla[i])
#         m_chisla.append(min)
#     elif chisla[i] == s:
#         null = int(chisla[i])
#         n_chisla.append(null)
#     elif chisla[i] > s:
#         max = int(chisla[i])
#         b_chisla.append(max)
# print("Среднее значение равно:", s, '\n',"Все числа:\n",  chisla, '\n', 'Числа меньше среднего:\n', m_chisla, '\n', "Числа равные среднему:\n", n_chisla, '\n', "Числа больше среднего:\n", b_chisla)

#NUM 8
# x_chisla = []
# y_chisla = []
# x2_chisla = []
# xy_chisla = []
# k = 0
# a = 0
# d = 0
# xy = 0
# while a != '':
#     x = float(input("Введите значения x\n"))
#     x_chisla.append(x)
#     y = float(input("Введите значения y\n"))
#     y_chisla.append(y)
#     d = x**2
#     x2_chisla.append(d)
#     xy = x * y
#     xy_chisla.append(xy)
#     k += 1
#     a = input("Если хотите закончить - нажмите Enter, иначе введите любой символ\n")
# m = (sum(xy_chisla) - (sum(x_chisla) * sum(y_chisla))/k)/(sum(x2_chisla) - (sum(x_chisla)**2)/k)
# b = sum(y_chisla)/k - m * (sum(x_chisla)/k)
# m = float('{:.3f}'.format(m))
# b = float('{:.3f}'.format(b))
# print('y =', m, 'x', '+', b)

