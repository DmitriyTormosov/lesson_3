#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month=int(input("введите месяц в виде целого числа: "))

spisok={
    12:"Зима", 1:"Зима", 2:"Зима", 3:"Весна", 4:"Весна", 5:"Весна", 6:"Лето", 7:"Лето",8:"Лето", 9:"осень", 10:"осень", 11:"осень"}

print(spisok[month])