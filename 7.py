#NUM 7
a = 0
k = 0
b = 0
chisla = []
m_chisla = []
n_chisla = []
b_chisla = []
while b != '':
    n = int(input("Введите число.\n"))
    chislo = int(n)
    chisla.append(chislo)
    a += n
    k += 1
    b = input("Если хотите закончить, нажмите Enter. Если нет, введите любой символ\n")
s = a / k
for i in range(0, k):
    if chisla[i] < s:
        min = int(chisla[i])
        m_chisla.append(min)
    elif chisla[i] == s:
        null = int(chisla[i])
        n_chisla.append(null)
    elif chisla[i] > s:
        max = int(chisla[i])
        b_chisla.append(max)
print("Среднее значение равно:", s, '\n',"Все числа:\n",  chisla, '\n', 'Числа меньше среднего:\n', m_chisla, '\n', "Числа равные среднему:\n", n_chisla, '\n', "Числа больше среднего:\n", b_chisla)