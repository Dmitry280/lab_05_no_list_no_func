""" Лабораторная работа №5: программа вычисления суммы ряда (по варианту) с точностью
до члена ряда ε.
Программа должна позволять задать значение аргумента (если требуется по варианту),
точность, максимальное количество итераций и шаг печати. Необходимо вывести таблицу
промежуточных вычислений с заданным шагом (номер итерации, значение текущего члена,
промежуточное значение суммы) и результат - вычисленное значение суммы ряда либо сообщение
о том, что за указанное число итераций необходимой точности достичь не удалось.
Автор: Дурбале Д.А. ИУ7-31БВ
Вариант №32:
+-------------+---+---+
| № итерации | t | s |
+-----------+---+---+
Использование пользовательских функций и списков запрещено
"""

from math import pow

s_sum = 0  # значение промежуточной суммы
tn = 0  # значение текущего члена

# блок ввода
i_count = float(input("Input the max iteration count: "))
eps = float(input("Input the precision value (ε): "))  # сумма будет вычисляться до тех пор пока |tn - t0| > eps
step = int(input("Input the printing step: "))  # шаг между строками в таблице
n = 1  # стартовый номер текущего члена
t0 = 0  # предыдущее значение текущего члена
max_sum_len = 0
max_tn_len = 0

# рассчитываем ширину столбцов
for i in range(1, int(i_count + 1)):
    tn = 1 / (pow((n + 1), 2) * pow((n + 2), 2))
    if len(str(tn)) > max_tn_len:
        max_tn_len = len(str(tn))
        t0 = tn
        s_sum = s_sum + t0
    if len(str(sum)) > max_sum_len:
        max_sum_len = len(str(sum))

# выводим шапку таблицы
print('+', len("Iteration №:") * '-', '+', max_tn_len * '-', '+', max_sum_len * '-', '+')
print('|', "Iteration №:".center(len("Iteration №:")), '|', "tn".center(max_tn_len), '|', 'S'.center(max_sum_len), '|')
print('+', len("Iteration №:") * '-', '+', max_tn_len * '-', '+', max_sum_len * '-', '+')

s_sum = 0  # обнуляем значение промежуточной суммы
tn = 0
# выводим тело таблицы
for count in range(1, int(i_count) + 1):
    tn = 1 / (pow((n + 1), 2) * pow((n + 2), 2))
    # tn = n * 2
    s_sum = s_sum + tn
    if count == 1 or count % step == 0:
        print('|', f"{count}".center(len("Iteration №:")), '|', f"{tn:.5g}".center(max_tn_len), '|',
              f"{s_sum:.5g}".center(max_sum_len), '|')
        print('+', len("Iteration №:") * '-', '+', max_tn_len * '-', '+', max_sum_len * '-', '+')
    if count == i_count:
        if abs(tn - t0) >= eps:
            print(
                f"Oops.. Within the specified number of iterations ({i_count})"
                f" the required accuracy ({eps}) could not be achieved... Please, try later.")
            print(f"eps = {eps}", "and", f"|tn - t0| = {abs(tn - t0)}")
    if count > 1:
        if abs(tn - t0) <= eps:
            print(f"The sum of the infinite series is: {s_sum:.5g},  reached within {count} iterations")
            print(f"eps = {eps}", "and",  f"|tn - t0| = {abs(tn - t0)}")
            break
    t0 = tn
    n += 1
