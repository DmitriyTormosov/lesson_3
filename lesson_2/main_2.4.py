#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

text=input("Введите предложение: ").split()
for i, text_2 in enumerate(text):
    print(i+1, text_2[:10])