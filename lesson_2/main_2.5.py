#Реализовать структуру «Рейтинг»,
# представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
my_list.append(int(input("Введите рейтинг: ")))
my_list=sorted(my_list,reverse=True)
print(my_list)