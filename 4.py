#NUM 4
words = []
n_words = []
line = str(input("Введите слово для добавления в список. Для окончания ввода, нажмите Enter\n"))
while line != '':
    slovo = str(line)
    words.append(slovo)
    line = str(input("Введите слово для добавления в список. Для окончания ввода,нажмите Enter\n"))
for w in words:
    if w not in n_words:
        n_words.append(w)
print("Старый список:\n", words, '\n', "Новый список:\n", n_words)
