#Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

b_rezult=float(input("Введите результат который следует добиться: "))
a_start=float(input("Введите показатели первого дня: "))
day=1 #количество дней
print(f"{day}-й день: {a_start}")
while a_start < b_rezult:
    a_start=float(a_start * 0.1 + a_start)
    day=day + 1

    print(f"{day}-й день: {a_start:.2f}")

print(f"На {day} день спортсмен достиг результата - не менее {int(b_rezult)} км.")
