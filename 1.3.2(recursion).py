#Виконав: Лавренюк Б.В., 1 курс, 122Г, ФТФ
#2. Сформувати функцію для обчислення цифрового кореню натурального числа.
#Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
#числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
#сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
#числа.
from time import time

q = int(input())

def d_r(q):
    w = str(q)
    q = sum([int(q) for q in w])
    if q > 9:
        return d_r(q)
    return q

start = time()
print(d_r(q))
stop = time()
print('Затрачений час: ', stop - start)
#не впевнений, але наверно тут теж складність алгоритму O(n)
#тут, на мою думку, рекурсивний метод легше зрозумілий за ітеративний
