#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
#натурального числа n.
from time import time

n = int(input())

def factorial(n):
    fact = 1
    while n > 1:       #Наталія Артурівна, коментарі допишу трохи пізніше, бо трохи немаю часу
        fact *= n
        n -= 1
    return fact

start = time()
print(factorial(n))
stop = time()
print('Затрачений час: ', stop - start)
#складність алгоритму O(n)
#читабельність коду: тут даже не знаю, шо писати. Але, на мою думку, ітераційний варіант
#легше зрозуміти, чим рекурсивний, бо в рекурсії треба розбиратись, щоб її розуміти.
