#NUM 5
chisla = []
m_chisla = []
n_chisla = []
p_chisla = []
line = int(input("Введите число для добавления в список. Для окончания ввода, введите 00\n"))
try:
    while list != '':
        if line < 0:
            minus = int(line)
            m_chisla.append(minus)
            line = int(input("Введите число для добавления в список. Для окончания ввода,нажмите Enter\n"))
        elif line == 0:
            null = int(line)
            n_chisla.append(null)
            line = int(input("Введите число для добавления в список. Для окончания ввода,нажмите Enter\n"))
        elif line > 0:
            plus = int(line)
            p_chisla.append(plus)
            line = int(input("Введите число для добавления в список. Для окончания ввода, нажмите Enter\n"))
except ValueError:
    list == ''
print(m_chisla, n_chisla, p_chisla)