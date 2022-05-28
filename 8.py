#NUM 8
x_chisla = []
y_chisla = []
x2_chisla = []
xy_chisla = []
k = 0
a = 0
d = 0
xy = 0
while a != '':
    x = float(input("Введите значения x\n"))
    x_chisla.append(x)
    y = float(input("Введите значения y\n"))
    y_chisla.append(y)
    d = x**2
    x2_chisla.append(d)
    xy = x * y
    xy_chisla.append(xy)
    k += 1
    a = input("Если хотите закончить - нажмите Enter, иначе введите любой символ\n")
m = (sum(xy_chisla) - (sum(x_chisla) * sum(y_chisla))/k)/(sum(x2_chisla) - (sum(x_chisla)**2)/k)
b = sum(y_chisla)/k - m * (sum(x_chisla)/k)
m = float('{:.3f}'.format(m))
b = float('{:.3f}'.format(b))
print('y =', m, 'x', '+', b)
